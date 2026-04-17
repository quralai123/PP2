import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.center = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "images")

        # 1. фон
        self.bg = pygame.image.load(os.path.join(img_dir, "clock.png")).convert()
        self.bg_rect = self.bg.get_rect(center=self.center)
        
        # 2. микки
        self.mickey_body = pygame.image.load(os.path.join(img_dir, "mikkey.png")).convert_alpha()
        self.mickey_body = pygame.transform.smoothscale(self.mickey_body, (500, 500)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)

        # 3. РУКИ (СТРЕЛКИ)
        self.min_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_right.png")).convert_alpha()
        self.min_hand_orig = pygame.transform.smoothscale(self.min_hand_orig, (250, 300)) 
        
        self.sec_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_left.png")).convert_alpha()
        self.sec_hand_orig = pygame.transform.smoothscale(self.sec_hand_orig, (250, 220)) 

    def blit_rotate_pivot(self, surface, image, pos, originPos, angle):
        # Метод для вращения картинки вокруг заданной точки (плеча)
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
        surface.blit(rotated_image, rotated_image_rect)

    def render(self, surface):
        surface.fill((255, 255, 255))
        
        # Рисуем фон и тело
        surface.blit(self.bg, self.bg_rect.topleft)
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        #время
        now = datetime.datetime.now()

        sec_angle = -((now.second * 6) - 90)
        min_angle = -((now.minute * 6 + now.second / 10) - 90)
        min_pivot = (self.min_hand_orig.get_width() // 2, self.min_hand_orig.get_height() - 20)
        sec_pivot = (self.sec_hand_orig.get_width() - 20, self.sec_hand_orig.get_height() - 20)  
        self.blit_rotate_pivot(surface, self.min_hand_orig, self.center, min_pivot, min_angle)
        self.blit_rotate_pivot(surface, self.sec_hand_orig, self.center, sec_pivot, sec_angle)