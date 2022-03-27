import pygame.font
from settings import Settings

class Button:

    def __init__(self, screen, msg, x_position, y_position):
        if msg in ['PlayButton', 'SettingsButton', 'RecordsButton', 'ExitButton']:  # Загрузка изобрадений кнопок меню
            self.image = pygame.image.load(f"images/Menu/{msg}.bmp").convert_alpha()
        if msg in ['red_ship', 'yellow_ship', 'green_ship', 'black_ship']:  # Загрузка изображений кнопок настрек
            self.image = pygame.image.load(f"images/Settings/{msg}.bmp").convert_alpha()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Построение и выравнивание кнопки
        self.rect = self.image.get_rect()
        if msg in ['PlayButton', 'SettingsButton', 'RecordsButton', 'ExitButton']:  # Выравнивание кнопок меню
            self.rect.centery = self.screen_rect.centery + y_position
            self.rect.right = self.screen_rect.right - x_position + 20

        if msg in ['red_ship', 'yellow_ship', 'green_ship', 'black_ship']:  # Выравнивание кнопок меню
            self.rect.centery = self.screen_rect.centery + y_position
            self.rect.centerx = self.screen_rect.centerx + x_position

    def button_draw(self):
        self.screen.blit(self.image, self.rect)
