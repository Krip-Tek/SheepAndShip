import pygame
import funtions as f
from button import Button


class Menu:

    def __init__(self, g_settings, screen):

        self.g_set = g_settings
        self.screen = screen
        self.set_bk_color(g_settings.bk_color)
        self.screen_rect = self.screen.get_rect()
        self.buttons = self.button_init()
        self.pause_buttons = []

    def set_bk_color(self, color):
        self.backscreen = pygame.image.load(f"images/Menu/{color}.bmp")

    def button_move(self, mouse_x, mouse_y):
        if self.buttons[0].rect.collidepoint(mouse_x, mouse_y):
            self.buttons[0] = Button(self.screen,
                                     "PlayButton", 20, -200)
        else:
            self.buttons[0] = Button(self.screen,
                                     "PlayButton", 0, -200)

        if self.buttons[1].rect.collidepoint(mouse_x, mouse_y):
            self.buttons[1] = Button(self.screen,
                                     "SettingsButton", 20, -75)
        else:
            self.buttons[1] = Button(self.screen,
                                     "SettingsButton", 0, -75)

        if self.buttons[2].rect.collidepoint(mouse_x, mouse_y):
            self.buttons[2] = Button(self.screen,
                                     "RecordsButton", 20, 50)
        else:
            self.buttons[2] = Button(self.screen,
                                     "RecordsButton", 0, 50)

        if self.buttons[3].rect.collidepoint(mouse_x, mouse_y):
            self.buttons[3] = Button(self.screen,
                                     "ExitButton", 20, 175)
        else:
            self.buttons[3] = Button(self.screen,
                                     "ExitButton", 0, 175)

    def button_init(self):

        play_button = Button(self.screen,
                             "PlayButton", 0, -200)
        settings_button = Button(self.screen,
                                 "SettingsButton", 0, -75)
        records_button = Button(self.screen,
                                "RecordsButton", 0, 50)
        exit_button = Button(self.screen,
                             "ExitButton", 0, 175)
        return_button = Button(self.screen,
                               "PlayButton", 0, -200)
        in_menu_button = Button(self.screen,
                                "ExitButton", 0, 175)

        self.buttons = [play_button, settings_button, records_button, exit_button]
        self.pause_buttons = [return_button, in_menu_button]
        return self.buttons

    def check_event(self, rifs, players, g_settings, screen, ship, sail):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                f.check_play_button(rifs, self.g_set,
                                    self.button_init(),
                                    mouse_x, mouse_y, players, screen, ship, sail)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if g_settings.game_active:
                        g_settings.pause_flag = True
                        g_settings.game_active = False
                    else:
                        g_settings.pause_flag = False
                        g_settings.game_active = True

                elif event.key == pygame.K_LALT and event.key == pygame.K_F4:
                    self.g_set.game_active = False
                    self.g_set.menu_flag = False
                    self.g_set.ALL_game = False

            elif self.g_set.game_active:
                if event.type == pygame.KEYDOWN:
                    f.pause_start(event, self.g_set)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            self.button_move(mouse_x, mouse_y)

    def backscreen_blit(self):
        self.screen.blit(self.backscreen, self.screen_rect)

    def button_draw(self):
        for but in self.buttons:
            but.button_draw()

    def menu_load(self, rifs, players, g_settings, screen, ship, sail):
        pygame.mixer.music.stop()
        f.menu_music('ship_song_menu', g_settings)
        while self.g_set.menu_flag:
            self.check_event(rifs, players, g_settings, screen, ship, sail)
            self.set_bk_color(g_settings.bk_color)
            self.backscreen_blit()
            self.button_draw()
            pygame.display.update()

    def pause_load(self, rifs, players, g_settings, screen, ship, sail):
        while self.g_set.pause_flag:
            self.check_event(rifs, players, g_settings, screen, ship, sail)
            self.pause_buttons[0].button_draw()
            self.pause_buttons[1].button_draw()

            pygame.display.update()

            if not self.g_set.pause_flag:
                break
