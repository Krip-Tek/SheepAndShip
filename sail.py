import pygame
import math
from ship import Ship


class Sail(pygame.sprite.Sprite):
    """Парус"""

    def __init__(self, screen, g_s):
        pygame.sprite.Sprite.__init__(self)
        self.g_s = g_s
        self.screen = screen
        ship = Ship(screen, g_s)
        self.image = pygame.image.load(f"images/SailSkin/black_sail.bmp")
        self.rect = self.image.get_rect()
        # ship.rect
        # self.sc_rect = screen.get_rect()
        # self.rect.centerx = float(self.sc_rect.centerx)
        # g_s.ship_cord = float(self.rect.centerx)
        # self.rect.bottom = self.sc_rect.bottom - 150

        self.rect.center = ship.rect.center
        # self.rect.centery = self.screen_rect.bottom - 80

    # def update(self, sp):
    #     """Движение корабля"""
    #     if self.rect.left <= 0:
    #         self.g_s.ship_speed = math.fabs(self.g_s.ship_speed)
    #     if self.rect.right >= self.sc_rect.right:
    #         self.g_s.ship_speed = -self.g_s.ship_speed
    #
    #     self.rect.centerx += self.g_s.ship_speed * self.g_s.kof
    def rotate_sail(self, image, angle):
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

    def sail_skin_load(self, color_name):
        """Загрузка скинов из директории"""
        self.image = pygame.image.load(f"images/SailSkin/{color_name}.bmp")

    def sail_blit(self, image, rect):
        """Отрисовка корабля"""
        self.screen.blit(image, rect)
