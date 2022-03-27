import pygame
import funtions as f
from button import Button
from ship import Ship

class GameSettings:

    def __init__(self, g_settings, screen, ship):

        self.g_set = g_settings
        self.screen = screen
        self.ship = ship
        self.backscreen = pygame.image.load(f"images/Settings/Settings_back.bmp")
        self.screen_rect = self.screen.get_rect()
        self.buttons = self.button_init()

    def check_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.g_set.g_settings_flag = False
                    self.g_set.menu_flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                f.ship_skin_set(self.g_set, self.buttons, mouse_x, mouse_y,self.ship)


    def button_init(self):

        red_ship = Button(self.screen,
                             "red_ship", -260, -10)
        yellow_ship = Button(self.screen,
                                 "yellow_ship", 100, -10)
        green_ship = Button(self.screen,
                                "green_ship", 285, -10)
        black_ship = Button(self.screen,
                             "black_ship", -82, -10)

        self.buttons = [red_ship, yellow_ship, green_ship, black_ship]
        return self.buttons

    def backscreen_blit(self):
        self.screen.blit(self.backscreen, self.screen_rect)

    def button_draw(self):
        for but in self.buttons:
            but.button_draw()

    def g_set_load(self):
        while self.g_set.g_settings_flag:

            self.check_event()
            self.backscreen_blit()
            self.button_draw()

            pygame.display.update()
