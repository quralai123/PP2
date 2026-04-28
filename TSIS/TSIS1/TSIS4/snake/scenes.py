import pygame
from pygame.locals import *
import sys
from code import DBManager

class Title:
    def __init__(self, game):
        self.game = game
        self.username = ""
        self.font = pygame.font.SysFont('Arial', 30)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Нажал Enter
                    if len(self.username) > 0:
                        self.game.current_username = self.username
                        self.game.state = Playing(self.game)
                elif event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    # Добавляем только буквы и цифры, ограничение 15 символов
                    if len(self.username) < 15 and event.unicode.isalnum():
                        self.username += event.unicode

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))
        title_text = self.font.render('SNAKE GAME', True, (0, 255, 0))
        prompt_text = self.font.render('Enter Name & Press ENTER:', True, (255, 255, 255))
        name_text = self.font.render(self.username + "_", True, (255, 255, 0))
        
        screen.blit(title_text, (200, 150))
        screen.blit(prompt_text, (130, 200))
        screen.blit(name_text, (240, 300))

class Playing:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.level = 1
        self.personal_best = self.game.db.get_personal_best(self.game.current_username)
        self.game.snake.__init__()
        self.game.food.respawn(self.game.snake.body) 
    

    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                # --- ТЕСТОВАЯ КНОПКА (УДАЛИТЬ ПОТОМ) ---
                if event.key == K_e:
                    self.game.last_score = self.score
                    self.game.db.save_result(
                        self.game.current_username, 
                        self.score, 
                        self.level
                    )
                    self.game.state = GameOver(self.game)
                # ---------------------------------------

                if event.key == K_UP: self.game.snake.change_direction('UP')
                elif event.key == K_DOWN: self.game.snake.change_direction('DOWN')
                elif event.key == K_LEFT: self.game.snake.change_direction('LEFT')
                elif event.key == K_RIGHT: self.game.snake.change_direction('RIGHT')
        
    def update(self):
        head = self.game.snake.body[0]
        # 1. Проверяем, наступила ли голова на еду ПЕРЕД движением
        ate_food = (head == self.game.food.position)
        
        # 2. Если еда протухла и не съедена — респавним
        if self.game.food.is_expired() and not ate_food:
            self.game.food.respawn(self.game.snake.body)

        # 3. Логика поедания (до движения змейки)
        if ate_food:
            if self.game.food.is_poison:
                # --- ЯД ---
                if len(self.game.snake.body) <= 3:
                    # Смерть, если длина станет <= 1
                    self.game.last_score = self.score
                    self.game.db.save_result(self.game.current_username, self.score, self.level)
                    self.game.state = GameOver(self.game)
                    return 
                else:
                    # Уменьшаем змейку
                    self.game.snake.body.pop()
                    self.game.snake.body.pop()
            else:
                # --- ОБЫЧНАЯ ЕДА ---
                self.score += self.game.food.weight
            
            # Респавн после еды
            self.game.food.respawn(self.game.snake.body)
            
            # Уровень
            if self.score // 5 >= self.level and self.level < 10:
                self.level += 1

        # 4. ДВИЖЕНИЕ
        # Растем, только если съели ОБЫЧНУЮ еду
        is_normal_growth = ate_food and not self.game.food.is_poison
        self.game.snake.move(grow=is_normal_growth)
        
        # 5. Проверка на столкновение с собой ПОСЛЕ движения
        new_head = self.game.snake.body[0]
        if new_head in self.game.snake.body[1:]:
            self.game.last_score = self.score
            self.game.db.save_result(self.game.current_username, self.score, self.level)
            self.game.state = GameOver(self.game)
    def draw(self, screen):
        screen.fill((20, 20, 20))
        if self.game.food.is_poison:
            food_color = ( 0, 0, 255) 
        else:
            # Если не ядовитая, берем цвета по весу из словаря
            colors = {1: (255, 0, 0), 2: (255, 255, 0), 3: (255, 0, 255)}
            food_color = colors.get(self.game.food.weight, (255, 0, 0))
        pygame.draw.rect(screen, food_color, (*self.game.food.position, 20, 20))
        
        for segment in self.game.snake.body:
            pygame.draw.rect(screen, (0, 200, 0), (*segment, 20, 20))
            
        font = pygame.font.SysFont('Arial', 20)
        info_text = font.render(f"Level: {self.level} | Weight: {self.game.food.weight}", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))

        font = pygame.font.SysFont('Arial', 20)
        info_text = font.render(
            f"| Score: {self.score} | Best: {max(self.personal_best, self.score)}", 
            True, (255, 255, 255)
        )
        screen.blit(info_text, (152, 10))
    
    def current_speed(self):
        return 10 + (self.level - 1) * 2
            
class GameOver:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont('Arial', 30)
        self.top_players = self.game.db.get_top_10()
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.state = Playing(self.game)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
    def update(self):
        pass


    def draw(self, screen):
        screen.fill((30, 30, 30))
        font_title = pygame.font.SysFont('Arial', 40)
        font_list = pygame.font.SysFont('Arial', 22)
        font_main = pygame.font.SysFont('Arial', 30)

        # 1. Заголовок
        header = font_title.render('GAME OVER', True, (255, 0, 0))
        screen.blit(header, (200, 50))

        # 2. Таблица лидеров (Топ-10) по центру
        leader_title = font_list.render('-- TOP 10 LEADERS --', True, (255, 215, 0))
        screen.blit(leader_title, (210, 110))
        
        y_offset = 140
        for i, (name, score) in enumerate(self.top_players):
            color = (200, 200, 200)
            if name == self.game.current_username: color = (0, 255, 255) # Подсветим игрока
            
            row = font_list.render(f"{i+1}. {name}: {score}", True, color)
            screen.blit(row, (220, y_offset))
            y_offset += 25

        score_text = font_main.render(f'Player: {self.game.current_username} | Score: {self.game.last_score}', True, (0, 255, 0))
        screen.blit(score_text, (130, 420))

        # 4. Подсказка по управлению
        retry = font_list.render('SPACE to restart OR Q to quit', True, (255, 255, 255))
        screen.blit(retry, (180, 480))

