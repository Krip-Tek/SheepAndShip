import pygame


class New_game_intro:
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
                pygame.time.wait(500)

        else:
            self.g_set.alpha -= 4
            if self.g_set.alpha <= 0:
                self.g_set.alpha_flag = 1
                self.g_set.intro_flag += 1

    def intro_load(self):
        self.g_set.intro_flag = 1
        self.set_intro(self.g_set.intro_flag)
        self.intro_rect = self.intro_bk.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.intro_rect.center = self.screen_rect.center

        self.intro_bk_blit()

        while self.g_set.intro_flag <= 6:
            self.check_event()
            self.set_intro(self.g_set.intro_flag)
            self.intro_drow()
            pygame.time.wait(10)
            self.intro_bk_blit()
            pygame.display.flip()
            if self.g_set.intro_flag == 3:
                pass

    def set_intro(self, i):
        self.intro_bk = pygame.image.load(f"images/Intro/Intro_game_{i}.bmp")

    def black_fill(self):
        self.screen.fill('black')

    def intro_bk_blit(self):
        self.black_fill()
        self.intro_bk.set_alpha(self.g_set.alpha)
        self.screen.blit(self.intro_bk, self.intro_rect)


