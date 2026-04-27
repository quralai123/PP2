import pygame
from pygame.locals import *
import sys

class Title:
    def __init__(self, game):
        self.game = game
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.state = Playing(self.game)
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Arial', 40)
        text = font.render('Press SPACE to Start', True, (255, 255, 255))
        screen.blit(text, (130, 250))
    
class Playing:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.level = 1
        self.game.snake.__init__()
        self.game.food.respawn(self.game.snake.body) # Пересоздаем еду при старте
        
    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP: self.game.snake.change_direction('UP')
                elif event.key == K_DOWN: self.game.snake.change_direction('DOWN')
                elif event.key == K_LEFT: self.game.snake.change_direction('LEFT')
                elif event.key == K_RIGHT: self.game.snake.change_direction('RIGHT')
        
    def update(self):
        # Проверяем, съела ли змейка еду
        ate_food = (self.game.snake.body[0] == self.game.food.position)
        
        # Требование: исчезновение еды по таймеру
        if self.game.food.is_expired() and not ate_food:
            self.game.food.respawn(self.game.snake.body)

        self.game.snake.move(grow=ate_food)
        head = self.game.snake.body[0]
        
        if ate_food:
            # Требование: начисление очков согласно весу еды
            self.score += self.game.food.weight
            self.game.food.respawn(self.game.snake.body)
            
            # Повышение уровня за каждые 5 очков
            if self.score // 5 >= self.level and self.level < 10:
                self.level += 1    
            
        # Проверка столкновения с самим собой
        if head in self.game.snake.body[1:]:
            self.game.state = GameOver(self.game)
        
    def draw(self, screen):
        screen.fill((20, 20, 20))
        
        # Отрисовка еды (Цвет меняется в зависимости от веса для наглядности)
        colors = {1: (255, 0, 0), 2: (255, 255, 0), 3: (255, 0, 255)}
        food_color = colors.get(self.game.food.weight, (255, 0, 0))
        pygame.draw.rect(screen, food_color, (*self.game.food.position, 20, 20))
        
        # Отрисовка змейки
        for segment in self.game.snake.body:
            pygame.draw.rect(screen, (0, 200, 0), (*segment, 20, 20))
            
        # Отрисовка интерфейса
        font = pygame.font.SysFont('Arial', 20)
        info_text = font.render(f"Level: {self.level} Score: {self.score} Weight: {self.game.food.weight}", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))
    
    def current_speed(self):
        return 10 + (self.level - 1) * 2
            
class GameOver:
    def __init__(self, game):
        self.game = game
        
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
        screen.fill((50, 0, 0))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Game Over! Press SPACE to restart OR Q to quit', True, (255, 255, 255))
        screen.blit(text, (25, 250))
        