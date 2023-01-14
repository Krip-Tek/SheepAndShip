import pygame
import math

class Ship:
    """Корабль"""

    def __init__(self, screen, g_s):
        self.color_path = g_s.color_path
        self.skin = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Default skin
        # Speed list
        self.s_l = [[[(0.5, -0.5), (0.25, 0), (0, 0)],  # Speed list
                     [(0.25, -0.25), (0, 0), (0, 0)],
                     [(0, 0), (0, 0), (0, 0)]],

                    [[(0.25, -0.25), (0.75, 0), (0.25, 0.25)],
                     [(0.5, -0.5), (0.5, 0), (0, 0)],
                     [(0.25, -0.25), (0, 0), (0, 0)]],

                    [[(0, 0), (0.25, 0), (0.5, 0.5)],
                     [(0.25, -0.25), (1, 0), (0.25, 0.25)],
                     [(0.5, -0.5), (0.25, 0), (0, 0)]],

                    [[(0, 0), (0, 0), (0.25, 0.25)],
                     [(0, 0), (0.5, 0), (0.5, 0.5)],
                     [(0.25, -0.25), (0.75, 0), (0.25, 0.25)]],

                    [[(0, 0), (0, 0), (0, 0)],
                     [(0, 0), (0, 0), (0.25, 0.25)],
                     [(0, 0), (0.25, 0), (0.5, 0.5)]]]

        self.g_s = g_s
        self.image = pygame.image.load(f"images/ShipSkin/{g_s.color_path}/5.bmp")
        self.rect = self.image.get_rect()
        self.sc = screen
        self.sc_rect = screen.get_rect()
        self.rect.centerx = float(self.sc_rect.centerx)
        g_s.ship_cord = float(self.rect.centerx)
        self.rect.bottom = self.sc_rect.bottom - 150

    def speed_up(self, as_list_speed):
        """Укорение игрока, реализующее инерционность движения корабля"""
        try:
            if self.g_s.ship_speed < as_list_speed:
                speed_up = 0.2
            elif self.g_s.ship_speed > as_list_speed:
                speed_up = -0.2
            else:
                speed_up = 0
            return speed_up
        except Exception:
            print("Что то случилось с ускорением!!!")

    def update(self, sp):
        """Движение корабля"""
        if self.rect.left <= 0:
            self.g_s.ship_speed = math.fabs(self.g_s.ship_speed)
        if self.rect.right >= self.sc_rect.right:
            self.g_s.ship_speed = -self.g_s.ship_speed
        speed_up = self.speed_up(sp)
        self.g_s.ship_speed = (self.g_s.ship_speed+speed_up)*self.g_s.kof
        self.g_s.ship_cord += self.g_s.ship_speed
        self.rect.centerx = self.g_s.ship_cord


    def sc_up(self, i, j):
        """Обновление скина корабля"""
        self.image = self.skin[i][j]

    def ship_skin_load(self, color_path):
        """Загрузка скинов из директории"""
        path = 1
        for i in range(0, 3):
            for j in range(0, 3):
                self.skin[i][j] = pygame.image.load(f"images/ShipSkin/{color_path}/"+str(path)+".bmp")
                path += 1


    def blit(self):
        """Отрисовка корабля"""
        self.sc.blit(self.image, self.rect)
