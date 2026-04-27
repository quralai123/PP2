import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((1366, 720))
    clock = pygame.time.Clock()
    
    radius = 10
    mode = 'blue'  # Режимы: 'red', 'green', 'blue', 'rect', 'circle'
    points = []
    
    drawing = False
    start_pos = None

    while True:
        screen.fill((0, 0, 0))
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                
                # Переключение режимов
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                elif event.key == pygame.K_s: mode = 'rect'   # S - Square (Rect)
                elif event.key == pygame.K_c: mode = 'circle' # C - Circle
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # ЛКМ
                    drawing = True
                    start_pos = event.pos
                    if mode in ['red', 'green', 'blue']:
                        points.append(event.pos)
                
                # Изменение радиуса (толщины)
                if event.button == 4: # Колесико вверх
                    radius = min(200, radius + 2)
                elif event.button == 5: # Колесико вниз
                    radius = max(1, radius - 2)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    # Если нужно, чтобы фигуры оставались, их нужно сохранять в отдельный список
                    # Но сейчас они работают как "превью"

            if event.type == pygame.MOUSEMOTION:
                if drawing and mode in ['red', 'green', 'blue']:
                    position = event.pos
                    points.append(position)
                    points = points[-256:] # Ограничение длины шлейфа

        # --- ОТРИСОВКА ШЛЕЙФА ---
        if mode in ['red', 'green', 'blue']:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        # --- ОТРИСОВКА ФИГУР (ПРЕВЬЮ) ---
        if drawing and start_pos and mode in ['rect', 'circle']:
            current_pos = pygame.mouse.get_pos()
            # Цвет для фигур сделаем ярким
            color = (255, 255, 255)
            
            if mode == 'rect':
                # Вычисляем rect (x, y, width, height)
                x = min(start_pos[0], current_pos[0])
                y = min(start_pos[1], current_pos[1])
                width = abs(current_pos[0] - start_pos[0])
                height = abs(current_pos[1] - start_pos[1])
                pygame.draw.rect(screen, color, (x, y, width, height), radius)
            
            elif mode == 'circle':
                # Радиус — расстояние от центра до курсора
                r = int(math.hypot(current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
                pygame.draw.circle(screen, color, start_pos, r, radius)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    # Логика затухания цвета
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue': color = (c1, c1, c2)
    elif color_mode == 'red': color = (c2, c1, c1)
    elif color_mode == 'green': color = (c1, c2, c1)
    else: color = (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

if __name__ == "__main__":
    main()