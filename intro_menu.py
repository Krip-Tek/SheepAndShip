import pygame

from plsyer_name import Player_name_input


class Intro_Menu:
    def __init__(self, g_settings, screen):
        self.g_set = g_settings
        self.screen = screen

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and event.key == pygame.K_F4:
                    self.g_set.game_active = False
                    self.g_set.menu_flag = False
                    self.g_set.ALL_game = False

    def intro_drow(self):
        if self.g_set.alpha_flag == 1:
            self.g_set.alpha += 3
            if self.g_set.alpha >= 255:
                self.g_set.alpha_flag = 0
                if self.g_set.intro_flag == 2:
                    pygame.time.wait(5000)
                else:
                    pygame.time.wait(1000)

        else:
            self.g_set.alpha -= 4
            if self.g_set.alpha <= 0:
                self.g_set.alpha_flag = 1
                self.g_set.intro_flag += 1

    def intro_load(self):
        self.set_intro(self.g_set.intro_flag)
        self.intro_rect = self.intro_bk.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.intro_rect.center = self.screen_rect.center

        self.intro_bk_blit()

        while self.g_set.intro_flag <= 2:
            self.check_event()
            self.set_intro(self.g_set.intro_flag)
            self.intro_drow()
            pygame.time.wait(10)
            self.intro_bk_blit()
            pygame.display.flip()
            if self.g_set.intro_flag == 3:
                self.pl_name_in = Player_name_input(self.g_set, self.screen)
                self.name_in_intro()

    def set_intro(self, i):
        self.intro_bk = pygame.image.load(f"images/Intro/Intro_{i}.bmp")

    def black_fill(self):
        self.screen.fill('black')

    def intro_bk_blit(self):
        self.black_fill()
        self.intro_bk.set_alpha(self.g_set.alpha)
        self.screen.blit(self.intro_bk, self.intro_rect)

    def name_in_intro(self):
        self.intro_bk = pygame.image.load(f"images/Intro/Intro_{3}.bmp")
        self.intro_bk.set_alpha(255)
        self.screen.blit(self.intro_bk, self.intro_rect)
        self.g_set.name_in = self.pl_name_in.player_name_in()
