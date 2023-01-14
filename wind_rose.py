import pygame
from random import *


class WindRose(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/WindRose.bmp").convert_alpha()
        self.p_image = self.image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.left + 80
        self.rect.centery = self.screen_rect.bottom - 80

    # def wind_rose_turn(self, g_settings):
    #     image_orig = self.image
    #     old_center = self.rect.center
    #     ang = g_settings.wind_rose_angle = randrange(-46, 46, 45)+1
    #     new_image = pygame.transform.rotate(image_orig, ang)
    #     self.p_image = new_image
    #     self.rect = new_image.get_rect()
    #     self.rect.center = old_center
    #
    #     if ang == 90:
    #         g_settings.w = 0
    #     elif ang == 45:
    #         g_settings.w = 1
    #     elif ang == 0:
    #         g_settings.w = 2
    #     elif ang == -45:
    #         g_settings.w = 3
    #     elif ang == -90:
    #         g_settings.w = 4

    def wind_rose_bilt(self):
        self.screen.blit(self.p_image, self.rect)
