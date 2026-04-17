import pygame
import sys
import os 
from ball import Ball

SCREEN_WIDTH  = 1366
SCREEN_HEIGHT = 720
FPS           = 165

COLOR_BG      = (245, 245, 245)  
COLOR_GRID    = (220, 220, 220)  
COLOR_TEXT    = (60,  60,  80)
COLOR_ACCENT  = (80,  120, 220)

def draw_grid(screen, spacing=40):
    for x in range(0, SCREEN_WIDTH, spacing):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, spacing):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y))

def draw_ui(screen, ball, font_small):
    x, y = ball.get_position()

    pos_text = font_small.render(f"Position: ({x}, {y})", True, COLOR_TEXT)
    screen.blit(pos_text, (10, 10))

    hints = "← ↑ ↓ → Move  |  R Reset  |  Q Quit"
    hint_surf = font_small.render(hints, True, COLOR_ACCENT)
    screen.blit(hint_surf, hint_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 18)))

    r = ball.RADIUS
    step = ball.STEP
    near_edge = (x - r < step or x + r > SCREEN_WIDTH  - step or
                 y - r < step or y + r > SCREEN_HEIGHT - step)
    if near_edge:
        warn = font_small.render("boundary", True, (200, 100, 0))
        screen.blit(warn, warn.get_rect(topright=(SCREEN_WIDTH - 10, 10)))

def get_font(path, size):
    """Безопасная загрузка шрифта: если файл не найден, берем системный Arial"""
    if os.path.exists(path):
        return pygame.font.Font(path, size)
    return pygame.font.SysFont("Arial", size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    # ОПРЕДЕЛЕНИЕ ПУТИ
    base_path = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_path, "ponts", "circular-std-4.ttf")
    font_small = get_font(font_path, 20)

    ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_r:
                    ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_UP:
                    ball.move("up")
                elif event.key == pygame.K_DOWN:
                    ball.move("down")
                elif event.key == pygame.K_LEFT:
                    ball.move("left")
                elif event.key == pygame.K_RIGHT:
                    ball.move("right")

        screen.fill(COLOR_BG)
        draw_grid(screen)

        ball.draw(screen)
        draw_ui(screen, ball, font_small)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()