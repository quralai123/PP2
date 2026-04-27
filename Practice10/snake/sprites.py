import random
import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'RIGHT'
    
    def move(self, grow=False):
        head_x, head_y = self.body[0]
        if self.direction == 'RIGHT':
            new_head = (head_x + 20, head_y)
        elif self.direction == 'LEFT':
            new_head = (head_x - 20, head_y)
        elif self.direction == 'UP':
            new_head = (head_x, head_y - 20)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 20)
        
        # Телепортация через границы экрана
        new_head = (new_head[0] % 600, new_head[1] % 600)
            
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()
            
    def change_direction(self, new_direction):
        opposite = {'RIGHT': 'LEFT', 'LEFT': 'RIGHT', 'UP': 'DOWN', 'DOWN': 'UP'}
        if new_direction != opposite[self.direction]:
            self.direction = new_direction
    
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.weight = 1
        self.spawn_time = 0 # Время появления еды
        self.lifetime = 5000 # Время жизни еды в миллисекундах (5 секунд)
        self.respawn([])
        
    def respawn(self, snake_body):
        # Генерируем новую позицию, которой нет в теле змейки
        while True:
            new_pos = (random.randrange(0, 600, 20), random.randrange(0, 600, 20))
            if new_pos not in snake_body:
                self.position = new_pos
                break
        
        # Требование: Randomly generating food with different weights
        # Вес еды будет влиять на то, сколько очков получит игрок
        self.weight = random.randint(1, 3)
        
        # Фиксируем время появления для таймера исчезновения
        self.spawn_time = pygame.time.get_ticks()

    def is_expired(self):
        # Требование: Foods which are disappearing after some time
        current_time = pygame.time.get_ticks()
        return current_time - self.spawn_time > self.lifetime