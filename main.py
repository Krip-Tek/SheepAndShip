import pygame
import json

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from wind_rose import WindRose
from menu import Menu
from intro_menu import Intro_Menu

import funtions as f


def main():
    pygame.init()

    def run_game():

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        g_settings = Settings()
        screen = pygame.display.set_mode((g_settings.screen_wigth,
                                          g_settings.screen_height),)
        # pygame.SCALED | pygame.NOFRAME | pygame.RESIZABLE | pygame.FULLSCREEN
        int_set = Intro_Menu(g_settings, screen)
        # int_set.intro_load()  # Загрузка интро при запуске игры

        with open("records.json") as file:
            players = json.load(file)  # загрузка данных игроков о рекордах

        font = pygame.font.SysFont('Times New Roman', 35)

        surf = pygame.Surface((5, 5))

        menu = Menu(g_settings, screen)  # Инициализация меню

        rifs = Group()  # Инициализация группы спрайтов рифов
        wind_rose = WindRose(screen)  # Инициализация розы ветров

        ship = Ship(screen, g_settings)  # Инициализация корабля

        if players and g_settings.name_in in players.keys():
            g_settings.top_score = players[g_settings.name_in]
            g_settings.new_game_intro = False
        else:
            players[g_settings.name_in] = 0

        f.top_score(g_settings, font)

        key = 1
        while g_settings.ALL_game:

            if g_settings.menu_flag:
                menu.menu_load(rifs, players, g_settings, screen, ship)

            ship.ship_skin_load(g_settings.color_path)

            top_score = f.top_score(g_settings, font)
            t_score = f.score_comp(g_settings, font)

            f.screen_up(screen, g_settings, rifs, ship, t_score, top_score)
            ship.update(g_settings.ship_speed)
            ship.blit()

            image, rect = f.wind_rose_time(g_settings, wind_rose)
            wind_rose.wind_rose_bilt(image, rect)

            f.rif_spawn(screen, surf, g_settings, rifs)
            f.collied_rifs(ship, rifs, g_settings, players)
            pygame.display.update()
            while key:
                pygame.time.wait(500)
                key = 0
            f.check_event(g_settings, wind_rose, ship, players)


            clock.tick(g_settings.FPS)
            if g_settings.pause_flag:
                menu.pause_load(rifs, players, g_settings, screen, ship)

    run_game()
    pygame.quit()


if __name__ == "__main__":
    main()
