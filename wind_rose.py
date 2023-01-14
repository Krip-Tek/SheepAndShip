import pygame


class WindRose(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/WindRose.bmp").convert_alpha()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.left + 80
        self.rect.centery = self.screen_rect.bottom - 80

    def rotate_wind_rose(self, image, angle):
        center_image = (image.get_width() // 2, image.get_height() // 2)
        image = self.rotate(image, center_image, angle)  # Обратиться к объекту розы ветров
        rect = image.get_rect()
        rect.centerx = self.rect.centerx
        rect.centery = self.rect.centery
        return image, rect

    def rotate(self, img, pos, angle):
        w, h = img.get_size()
        img2 = pygame.Surface((w * 2, h * 2), pygame.SRCALPHA)
        img2.blit(img, (w - pos[0], h - pos[1]))
        return pygame.transform.rotate(img2, -angle)

    def wind_rose_bilt(self, image, rect):
        self.screen.blit(image, rect)
