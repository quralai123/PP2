import pygame
import random
from pygame.locals import *

# Константы
WIDTH = 400
HEIGHT = 600
SPEED = 3
SCORE = 0

LANES = [65, 155, 245, 335]

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/suanb/Desktop/pp2/TSIS/TSIS1/TSIS3/carracer/images_and_sounds/Player(1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.speed_multiplier = 1.0
        self.lives = 3  # Система жизней из нового кода
        self.shield_active = False

    def take_hit(self):
        if self.shield_active:
            self.shield_active = False
            return False # Выжил
        self.lives -= 1
        return self.lives <= 0 # True если Game Over

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        move_speed = 5 * self.speed_multiplier
        if self.rect.left > 10 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-move_speed, 0)
        if self.rect.right < WIDTH - 10 and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(move_speed, 0)

            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/suanb/Desktop/pp2/TSIS/TSIS3/carracer/images_and_sounds/Enemy(1).png")
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self, lane=None):
        if lane is None: lane = random.choice(LANES)
        self.rect.center = (lane, -100)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.spawn()

# Для препятствий (Barrier, Oil)
class RoadObstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        if type == "oil":
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (50, 50, 50), (20, 20), 20)
        else: # barrier
            self.image = pygame.Surface((60, 20))
            self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()

    def spawn(self, lane=None, offset_y=-100):
        if lane is None: lane = random.choice(LANES)
        self.rect.center = (lane, offset_y)

    def move(self):
        self.rect.move_ip(0, SPEED)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загружаем один раз, чтобы не перегружать память
        self.original_image = pygame.image.load("c:/Users/suanb/Desktop/pp2/TSIS/TSIS3/carracer/images_and_sounds/Coin.png")
        self.weight = 1
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.spawn() # Инициализируем через spawn

    def spawn(self, lane=None):
        """Создает монету в конкретной полосе с рандомным весом"""
        # Установка веса и размера (динамическая сложность)
        self.weight = random.randint(1, 5)
        size = 20 + self.weight * 5
        self.image = pygame.transform.scale(self.original_image, (size, size))
        
        # Позиционирование
        self.rect = self.image.get_rect()
        if lane is None:
            lane = random.choice(LANES)
        
        self.rect.center = (lane, -100)

    def reset(self):
        """Метод-заглушка для совместимости с кодом коллизий"""
        self.spawn()

    def move(self):
        # Используем глобальную скорость из модуля sprites
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.kill() # Если используем систему волн, лучше удалять и создавать новые