import pygame
import json


class Records:

    def __init__(self, g_setings, screen):
        self.g_set = g_setings
        self.screen = screen
        self.backscreen = pygame.image.load(f"images/Records/Settings_back.bmp")
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont('Times New Roman', 35)

    def check_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.g_set.p_record_flag = False
                    self.g_set.menu_flag = True

    def load_records(self):
        k = 0
        n = 180
        second_dict = {}
        with open("records.json") as file:
            players = json.load(file)

        for key, values in players.items():
            second_dict[values] = key

        board_keys = sorted(second_dict, reverse=True)

        if len(board_keys) < 5:
            j = len(board_keys)
        else:
            j = 5

        while k < j:
            text = self.font.render(f"{second_dict[board_keys[k]]}", True, (20, 20, 20))
            self.screen.blit(text, (550, 40+n))

            text = self.font.render(f"{board_keys[k]}", True, (20, 20, 20))
            self.screen.blit(text, (885, 40+n))
            n += 76
            k += 1

    def backscreen_blit(self):
        self.screen.blit(self.backscreen, self.screen_rect)

    def set_load(self):
        while self.g_set.p_record_flag:
            self.check_event()
            self.backscreen_blit()
            self.load_records()
            pygame.display.update()


