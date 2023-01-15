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
        self.image = pygame.image.load(f"images/SailSkin/red_sail.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = ship.rect.center

    def move_sail(self, ship):
        self.rect.center = ship.rect.center
        pass

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
