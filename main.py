import pygame
import json

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from wind_rose import WindRose
from menu import Menu

import funtions as f


def main():
    pygame.init()

    def run_game():
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        g_settings = Settings()

        g_settings.name_in = input("Введите ваше имя: ")

        with open("records.json") as file:
            players = json.load(file)

        screen = pygame.display.set_mode((g_settings.screen_wigth,
                                          g_settings.screen_height), pygame.SCALED)
        font = pygame.font.SysFont('Times New Roman', 35)
        surf = pygame.Surface((5, 5))

        pygame.display.set_caption("Мореход")
        menu = Menu(g_settings, screen)

        rifs = Group()
        wind_rose = WindRose(screen)

        ship = Ship(screen, g_settings)

        if players and g_settings.name_in in players.keys():
            g_settings.top_score = players[g_settings.name_in]
            print("С возращением, ", g_settings.name_in)

            print(f"Ваш последний рекорд, {g_settings.top_score}")
        else:
            players[g_settings.name_in] = 0
            print(f"{g_settings.name_in}, добро пожаловать")

        f.top_score(g_settings, font)

        while True:
            if g_settings.menu_flag:
                menu.menu_load(rifs, players, g_settings, screen,ship)
            ship.ship_skin_load(g_settings.color_path)

            top_score = f.top_score(g_settings, font)
            t_score = f.score_comp(g_settings, font)

            f.screen_up(screen, g_settings, rifs, ship, t_score, top_score)
            ship.update(g_settings.ship_speed)
            ship.blit()

            wind_rose.wind_rose_bilt()
            f.rif_spawn(screen, surf, g_settings, rifs)
            f.collied_rifs(ship, rifs, g_settings, players)
            pygame.display.update()
            f.check_event(g_settings, wind_rose, ship, players)

            clock.tick(g_settings.FPS)
            if g_settings.pause_flag:
                menu.pause_load(rifs, players, g_settings, screen, ship)

    run_game()


if __name__ == "__main__":
    main()
