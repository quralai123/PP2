import pygame
from pygame.locals import *
from scenes import Title, Playing
import sprites
import sys
from code import DBManager # Проверь, что этот импорт есть вверху
import json
import os

class SettingsManager:
    def __init__(self, filename="settings.json"):
        self.filename = filename
        self.defaults = {
            "snake_color": [152, 251, 152], # RGB Зеленый
            "grid_overlay": True,
            "sound": True
        }
        self.data = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return self.defaults.copy()

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

class Game:
    def __init__(self):
        self.db = DBManager() # 2. ОБЯЗАТЕЛЬНО С ЭТИМ ИМЕНЕМ
        self.current_username = "Guest"
        self.last_score = 0
        self.snake = sprites.Snake()
        self.food = sprites.Food()
        self.state = Title(self)
        self.settings = SettingsManager()
        # main.py -> class Game -> __init__
        pygame.mixer.init() # Инициализация звукового движка

        # Загрузка файлов (убедись, что файлы .wav или .mp3 лежат в папке с кодом)
        self.eat_sound = pygame.mixer.Sound("c:/Users/suanb/Desktop/pp2/TSIS/TSIS1/TSIS4/sounds/eat.mp3")
        self.poison_sound = pygame.mixer.Sound("c:/Users/suanb/Desktop/pp2/TSIS/TSIS1/TSIS4/sounds/poison.wav")
        self.powerup_sound = pygame.mixer.Sound("c:/Users/suanb/Desktop/pp2/TSIS/TSIS1/TSIS4/sounds/powerup.wav")
        self.death_sound = pygame.mixer.Sound("c:/Users/suanb/Desktop/pp2/TSIS/TSIS1/TSIS4/sounds/death.mp3")

def main():
    pygame.init()
    pygame.display.set_caption('Snake Game')

    # Константы экрана
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    # Инициализация объекта Game (в котором лежат настройки и БД)
    game = Game()
    
    # Устанавливаем начальное состояние — Экран ввода имени
    game.state = Title(game)
    
    while True:
        # 1. Получаем события ОДИН раз за цикл
        events = pygame.event.get()
        
        for event in events:
            if event.type == QUIT:
                # Если есть метод сохранения настроек, вызываем его перед выходом
                game.settings.save() 
                pygame.quit()
                sys.exit()
        
        # 2. Передаем список событий в текущее состояние (Title, Menu, Settings или Playing)
        game.state.handle_events(events)
        
        # 3. Обновляем логику (движение змейки, проверка бонусов, таймеры)
        game.state.update()
        
        # 4. Отрисовка
        game.state.draw(SCREEN)
        pygame.display.update()
        
        # 5. Управление скоростью (FPS)
        if isinstance(game.state, Playing):
            # Скорость меняется в зависимости от эффектов (Speed boost/Slow motion)
            clock.tick(game.state.current_speed())
        else:
            # В меню и настройках держим стабильные 30 FPS
            clock.tick(30)

if __name__ == '__main__':
    main()