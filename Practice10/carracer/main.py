import pygame 
import time, random
import sys
from pygame.locals import *
import sprites

def main():
    pygame.init()
    # Сбрасываем статы при старте
    sprites.SCORE = 0
    sprites.SPEED = 3

    FPS = 165
    FramePerSec = pygame.time.Clock()

    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, sprites.BLACK)

    background = pygame.image.load("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/Road.png")
    background = pygame.transform.scale(background, (400, 600))

    SCREEN = pygame.display.set_mode((sprites.WIDTH, sprites.HEIGHT))
    pygame.display.set_caption("Racer")
            
    P1 = sprites.Player()
    E1 = sprites.Enemy()
    C = sprites.Coin()

    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies.add(E1)
    coins.add(C)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C) 

    # Переменные для анимации бесконечного фона
    bg_y1 = 0
    bg_y2 = -sprites.HEIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Движение фона
        bg_y1 += sprites.SPEED
        bg_y2 += sprites.SPEED
        if bg_y1 >= sprites.HEIGHT: bg_y1 = -sprites.HEIGHT
        if bg_y2 >= sprites.HEIGHT: bg_y2 = -sprites.HEIGHT

        SCREEN.blit(background, (0, bg_y1))
        SCREEN.blit(background, (0, bg_y2))

        # Отрисовка счета
        scores = font_small.render("SCORES: " + str(sprites.SCORE), True, sprites.GREEN)        
        SCREEN.blit(scores, (10, 10))
        
        # Обновление и отрисовка всех объектов
        for entity in all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            entity.move()
            
        # Проверка столкновения с врагом
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/accident.mp3").play()
            time.sleep(0.5)
            
            SCREEN.fill(sprites.RED)
            # Центрируем надписи (Требование по оформлению)
            SCREEN.blit(game_over, game_over.get_rect(center=(sprites.WIDTH//2, 250)))
            
            font_restart = pygame.font.SysFont("Verdana", 20)
            retry_text = font_restart.render("R - Restart or Q - Quit", True, sprites.WHITE)
            SCREEN.blit(retry_text, retry_text.get_rect(center=(sprites.WIDTH//2, 350)))
            
            pygame.display.update()
            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r: main()
                        if event.key == K_q:
                            pygame.quit()
                            sys.exit()
            
        # Проверка сбора монет
        collided_coin = pygame.sprite.spritecollideany(P1, coins)
        if collided_coin:
            # 1. Прибавляем вес монетки (Разный вес монет)
            sprites.SCORE += collided_coin.weight 
            
            # 2. Увеличиваем скорость врагов каждые 10 очков (N монет)
            if sprites.SCORE % 10 == 0:
                sprites.SPEED += 0.5
            
            pygame.mixer.Sound("C:/Users/suanb/Desktop/pp2/Practice10/carracer/images_and_sounds/coin_taken.wav").play()
            collided_coin.reset() # Используем метод из sprites.py для респауна
        
        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    main()