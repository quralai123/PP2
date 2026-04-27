import pygame
from pygame.locals import *
import random
    
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 400
HEIGHT = 600
SPEED = 2
SCORE = 0    
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/Enemy(1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/Player(1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 20:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 20:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загружаем базовое изображение один раз при создании
        self.original_image = pygame.image.load("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/Coin.png")
        self.rect = self.original_image.get_rect()
        self.reset()

    def reset(self):
        # 1. Генерируем случайный вес (от 1 до 5)
        self.weight = random.randint(1, 5)
        
        # 2. МЕНЯЕМ РАЗМЕР в зависимости от веса (ВАША СТРОКА ТУТ)
        # Мы используем self.original_image, чтобы качество не портилось при масштабировании
        new_size = 20 + self.weight * 5
        self.image = pygame.transform.scale(self.original_image, (new_size, new_size))
        
        # 3. Обновляем rect, так как размер картинки изменился
        self.rect = self.image.get_rect()
        
        # 4. Ставим в случайную позицию наверху
        self.rect.top = -50
        self.rect.left = random.randint(20, WIDTH - self.rect.width - 20)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.reset()