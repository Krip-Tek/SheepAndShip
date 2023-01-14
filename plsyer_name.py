import pygame


class Player_name_input:
    def __init__(self, g_settings, screen):
        self.font = pygame.font.Font(None, 96)
        self.screen = screen
        self.g_set = g_settings
        self.clock = pygame.time.Clock()
        self.input_box = pygame.Rect(self.g_set.screen_width / 2 - 230, self.g_set.screen_height / 2 + 131, 440, 76)
        self.color_inactive = pygame.Color('black')
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.Text_in = True

    def player_name_in(self):
        while self.Text_in:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.Text_in = False
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.Text_in = False
                            return self.text

                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
            self.up_screen()
            txt_surface = self.font.render(self.text, True, 'lightskyblue3')
            width = max(440, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, self.color, self.input_box, 2)
            pygame.display.flip()
            self.clock.tick(30)

    def up_screen(self):
        self.intro_bk = pygame.image.load(f"images/Intro/Intro_{3}.bmp")
        self.intro_rect = self.intro_bk.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.intro_rect.center = self.screen_rect.center
        self.screen.blit(self.intro_bk, self.intro_rect)

