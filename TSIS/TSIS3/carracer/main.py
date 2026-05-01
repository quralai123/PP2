import pygame, sys, time, random
from pygame.locals import *
import sprites

# Конфигурация из нового кода
SPAWN_CHANCE = 0.03
MAX_OBSTACLES = 2

def has_free_lane(enemies, obstacles):
    """Проверка Safe Path (3.1): чтобы всегда была свободная полоса"""
    occupied = set()
    for obj in list(enemies) + list(obstacles):
        if obj.rect.top > 100: # Если объект близко к игроку
            for lane in sprites.LANES:
                if abs(obj.rect.centerx - lane) < 40:
                    occupied.add(lane)
    return len(occupied) < len(sprites.LANES)

def main():
    pygame.init()
    sprites.SCORE = 0
    sprites.SPEED = 3
    
    FPS = 60
    clock = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((sprites.WIDTH, sprites.HEIGHT))
    
    # Шрифты
    font_small = pygame.font.SysFont("Verdana", 18)
    font_big = pygame.font.SysFont("Verdana", 60)

    # Загрузка ресурсов
    background = pygame.image.load("c:/Users/suanb/Desktop/pp2/TSIS/TSIS3/carracer/images_and_sounds/Road.png")
    background = pygame.transform.scale(background, (400, 600))
    
    # События
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 2000) # Ускорение каждые 2 сек
    ROAD_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(ROAD_EVENT, 5000) # Пробки/Барьеры каждые 5 сек

    P1 = sprites.Player()
    
    # Группы
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(P1)

    bg_y1, bg_y2 = 0, -600

    while True:
        # ── Обработка событий ──
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == INC_SPEED:
                sprites.SPEED += 0.1 # Плавное усложнение (3.2)
            
            if event.type == ROAD_EVENT:
                # Создаем "пробку" в одной полосе (3.1 Road Events)
                blocked_lane = random.choice(sprites.LANES)
                for i in range(2):
                    obs = sprites.RoadObstacle("barrier")
                    obs.spawn(lane=blocked_lane, offset_y=-100 - i*150)
                    obstacles.add(obs); all_sprites.add(obs)

        # ── Динамический спавн (из твоего нового кода) ──
        if random.random() < SPAWN_CHANCE and has_free_lane(enemies, obstacles):
            lane = random.choice(sprites.LANES)
            if random.random() < 0.6: # Шанс врага
                new_enemy = sprites.Enemy()
                new_enemy.spawn(lane)
                enemies.add(new_enemy); all_sprites.add(new_enemy)
            else: # Шанс монетки
                new_coin = sprites.Coin()
                new_coin.spawn(lane)
                coins.add(new_coin); all_sprites.add(new_coin)

        # ── Логика движения ──
        bg_y1 = (bg_y1 + int(sprites.SPEED)) % 600
        bg_y2 = bg_y1 - 600
        
        SCREEN.blit(background, (0, bg_y1))
        SCREEN.blit(background, (0, bg_y2))

        for entity in all_sprites:
            entity.move()
            SCREEN.blit(entity.image, entity.rect)
            if entity != P1 and entity.rect.top > 600:
                entity.kill()

        # ── Коллизии ──
        # Враги
        if pygame.sprite.spritecollideany(P1, enemies):
            if P1.take_hit(): # Если жизни кончились
                # Вызов экрана Game Over
                print("GAME OVER")
                pygame.quit(); sys.exit()
            else:
                # Временное бессмертие или откат врага
                for e in enemies: e.kill()

        # Монеты
        coin_hit = pygame.sprite.spritecollideany(P1, coins)
        if coin_hit:
            sprites.SCORE += coin_hit.weight
            coin_hit.kill()

        # Препятствия (масло/барьеры)
        obs_hit = pygame.sprite.spritecollideany(P1, obstacles)
        if obs_hit:
            if obs_hit.type == "oil": P1.speed_multiplier = 0.4
            else: P1.speed_multiplier = 0.2
            obs_hit.kill()

        # Рекуперация скорости игрока
        P1.speed_multiplier += (1.0 - P1.speed_multiplier) * 0.05

        # ── Интерфейс (HUD) ──
        score_txt = font_small.render(f"Score: {sprites.SCORE}", True, (255, 255, 255))
        lives_txt = font_small.render(f"Lives: {P1.lives}", True, (255, 100, 100))
        SCREEN.blit(score_txt, (10, 10))
        SCREEN.blit(lives_txt, (10, 30))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()