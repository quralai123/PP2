import pygame
import sys
import math

# Инициализация
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1100, 750 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (180, 180, 180)
BLUE_SELECT = (0, 120, 215) 

PALETTE = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 0, 0)]

# Добавили 'Brush' в начало списка инструментов
TOOLS = [
    ('Brush', 'brush'), ('Rect', 'rectangle'), ('Circle', 'circle'), 
    ('Square', 'square'), ('R-Tri', 'right_triangle'), 
    ('E-Tri', 'equilateral_triangle'), ('Rhombus', 'rhombus'), ('Eraser', 'erase')
]

def draw_shape(surface, mode, start_pos, end_pos, color, thickness):
    x1, y1 = start_pos
    x2, y2 = end_pos
    if mode == 'rectangle':
        pygame.draw.rect(surface, color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), thickness)
    elif mode == 'square':
        side = max(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, (min(x1, x2), min(y1, y2), side, side), thickness)
    elif mode == 'circle':
        r = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start_pos, r, thickness)
    elif mode == 'right_triangle':
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif mode == 'equilateral_triangle':
        height = (y2 - y1)
        side = abs(height) * 2 / math.sqrt(3)
        pygame.draw.polygon(surface, color, [(x1, y1), (x1 - side/2, y2), (x1 + side/2, y2)], thickness)
    elif mode == 'rhombus':
        pygame.draw.polygon(surface, color, [((x1+x2)/2, y1), (x2, (y1+y2)/2), ((x1+x2)/2, y2), (x1, (y1+y2)/2)], thickness)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint with Brush and Shapes")
    clock = pygame.time.Clock()
    
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(WHITE)
    
    font = pygame.font.SysFont("Arial", 14, bold=True)
    current_color = PALETTE[0]
    mode = 'brush' # Теперь кисть по умолчанию
    drawing = False
    start_pos = None
    last_pos = None # Нужно для плавности кисти

    while True:
        screen.fill(WHITE)
        screen.blit(canvas, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < 60: # Клик в меню
                    for i, col in enumerate(PALETTE):
                        if pygame.Rect(10 + i * 40, 15, 30, 30).collidepoint(x, y):
                            current_color = col
                    for i, (name, m) in enumerate(TOOLS):
                        button_rect = pygame.Rect(260 + i * 90, 15, 85, 30)
                        if button_rect.collidepoint(x, y):
                            mode = m
                else: 
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    # Фиксируем фигуру, если это не кисть и не ластик
                    if mode not in ['brush', 'erase']:
                        draw_shape(canvas, mode, start_pos, event.pos, current_color, 2)
                    drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    curr_pos = event.pos
                    # КИСТЬ И ЛАСТИК рисуют сразу на холсте (canvas)
                    if mode == 'brush':
                        pygame.draw.line(canvas, current_color, last_pos, curr_pos, 3)
                        last_pos = curr_pos
                    elif mode == 'erase':
                        pygame.draw.circle(canvas, WHITE, curr_pos, 20)
                        last_pos = curr_pos

        # ОТРИСОВКА ПРЕВЬЮ ДЛЯ ФИГУР
        if drawing and mode not in ['brush', 'erase']:
            curr_pos = pygame.mouse.get_pos()
            draw_shape(screen, mode, start_pos, curr_pos, current_color, 2)

        # РИСУЕМ ПАНЕЛЬ (UI)
        pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 60))
        pygame.draw.line(screen, BLACK, (0, 60), (WIDTH, 60), 2)
        
        for i, col in enumerate(PALETTE):
            rect = pygame.Rect(10 + i * 40, 15, 30, 30)
            pygame.draw.rect(screen, col, rect)
            if col == current_color and mode not in ['erase']:
                pygame.draw.rect(screen, BLACK, rect, 2)

        for i, (name, m) in enumerate(TOOLS):
            btn_rect = pygame.Rect(260 + i * 90, 15, 85, 30)
            bg_color = BLUE_SELECT if mode == m else DARK_GRAY
            pygame.draw.rect(screen, bg_color, btn_rect, border_radius=5)
            text = font.render(name, True, WHITE if mode == m else BLACK)
            screen.blit(text, text.get_rect(center=btn_rect.center))

        pygame.display.flip()
        clock.tick(120) # 120 FPS для плавности кисти

if __name__ == "__main__":
    main()