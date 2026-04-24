import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE_SELECT = (0, 120, 215) 


PALETTE = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), 
    (255, 255, 0), (255, 0, 255), (0, 0, 0)
]

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint with UI")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Arial", 18, bold=True)
    
    screen.fill(WHITE)
    current_color = PALETTE[0]
    mode = 'circle'
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Выбор цвета
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] < 50:
                    for i, col in enumerate(PALETTE):
                        rect = pygame.Rect(10 + i * 40, 10, 30, 30)
                        if rect.collidepoint(event.pos):
                            current_color = col
                            if mode == 'erase': mode = 'circle'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_r: mode = 'rectangle'
                if event.key == pygame.K_e: mode = 'erase'

        
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            pos = pygame.mouse.get_pos()
            if pos[1] > 55:
                if mode == 'circle':
                    pygame.draw.circle(screen, current_color, pos, 10)
                elif mode == 'rectangle':
                    pygame.draw.rect(screen, current_color, (pos[0]-10, pos[1]-10, 20, 20))
                elif mode == 'erase':
                    pygame.draw.circle(screen, WHITE, pos, 20)

    
        # панель
        pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 50))
        pygame.draw.line(screen, BLACK, (0, 50), (WIDTH, 50), 2)
        
        # палитра
        for i, col in enumerate(PALETTE):
            rect = pygame.Rect(10 + i * 40, 10, 30, 30)
            pygame.draw.rect(screen, col, rect)
            if col == current_color and mode != 'erase':
                pygame.draw.rect(screen, WHITE, rect, 3) # Рамка выбора

        # текст
        text_circle = font.render("C — Круг", True, BLUE_SELECT if mode == 'circle' else BLACK)
        text_rect = font.render("R — Квадрат", True, BLUE_SELECT if mode == 'rectangle' else BLACK)
        text_erase = font.render("E — Ластик", True, BLUE_SELECT if mode == 'erase' else BLACK)
        
       
        screen.blit(text_circle, (280, 15))
        screen.blit(text_rect, (400, 15))
        screen.blit(text_erase, (540, 15))

        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()