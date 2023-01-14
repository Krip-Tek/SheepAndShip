import pygame
from pygame.sprite import Sprite


class Rif(Sprite):

    def __init__(self, position_x, position_y, screen, group, g_s):
        super().__init__()
        self.screen_r = screen
        self.g_s = g_s
        if not g_s.coin:
            self.image = pygame.image.load("images/Rif.bmp")
            self.coin = g_s.coin
        else:
            self.image = pygame.image.load("images/sheep_W.bmp")
            self.coin = g_s.coin
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.top = self.screen_rect.top - 100

        self.add(group)

    def update(self, height, speed):
        if self.y <= self.screen_rect.bottom:
            self.y += speed*self.g_s.kof
            self.y += speed
            self.rect.y = self.y
        else:
            self.kill()  # Удаление рифа который ушел за край экрана

    def get_rif_wigth(self):
        return self.rect.width
