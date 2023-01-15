import pygame
import math


class Ship(pygame.sprite.Sprite):
    """Корабль"""

    def __init__(self, screen, g_s):
        pygame.sprite.Sprite.__init__(self)

        self.g_s = g_s
        self.image = pygame.image.load(f"images/ShipSkin/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.sc_rect = screen.get_rect()
        self.rect.centerx = float(self.sc_rect.centerx)
        g_s.ship_cord = float(self.rect.centerx)
        self.rect.bottom = self.sc_rect.bottom - 150

    def update(self, g_s):
        """Движение корабля"""
        g_s.ship_speed = 1
        if self.rect.left <= 0 and g_s.ship_angle < 0:
            self.g_s.ship_speed = 0
        if self.rect.right >= self.sc_rect.right and g_s.ship_angle > 0:
            self.g_s.ship_speed = 0

        if g_s.ship_angle < 0:
            g_s.ship_cord -= g_s.ship_speed
        elif g_s.ship_angle > 0:
            g_s.ship_cord += g_s.ship_speed
        else:
            g_s.ship_speed = 0

        self.rect.centerx = g_s.ship_cord

    def rotate_ship(self, image, angle):
        center_image = (image.get_width() // 2, image.get_height() // 2)
        image = self.rotate(image, center_image, angle)
        rect = image.get_rect()
        rect.centerx = self.rect.centerx
        rect.centery = self.rect.centery
        return image, rect

    def rotate(self, img, pos, angle):
        w, h = img.get_size()
        img2 = pygame.Surface((w * 2, h * 2), pygame.SRCALPHA)
        img2.blit(img, (w - pos[0], h - pos[1]))
        return pygame.transform.rotate(img2, -angle)

    def ship_blit(self, image, rect):
        """Отрисовка корабля"""
        self.screen.blit(image, rect)
