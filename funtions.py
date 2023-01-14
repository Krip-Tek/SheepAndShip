import pygame
import json
from random import *

from rif import Rif
from game_settings import GameSettings
from records import Records
from new_game_intro import New_game_intro


def menu_music(sound_name, g_settings):  # Звуковое сопровождение
    pygame.mixer.music.load(f'sounds/{sound_name}.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(g_settings.music_volume)


def rotate(img, pos, angle):
    w, h = img.get_size()
    img2 = pygame.Surface((w * 2, h * 2), pygame.SRCALPHA)
    img2.blit(img, (w - pos[0], h - pos[1]))
    return pygame.transform.rotate(img2, angle)


def wind_rose_time(g_settings, wind_rose):  # Поворот розы ветров
    g_settings.wind_rose_step += 1
    if g_settings.wind_rose_step > g_settings.wind_rose_second:
        # wind_rose.wind_rose_turn(g_settings)
        g_settings.wind_rose_second = randrange(3, 5)  # Время поворота Розы Ветров от n до m секунд
        g_settings.wind_rose_step = 0


def score_save(g_s, players):  # Сохранение счёта игрока
    if g_s.score > int(g_s.top_score):
        g_s.top_score = g_s.score
        players[g_s.name_in] = g_s.top_score
    with open("records.json", "w") as file:
        json.dump(players, file, indent=4, ensure_ascii=False)


def top_score(g_s, f):
    top_scor = f.render("Рекорд: "+str(g_s.top_score), 1, (95, 0, 144))
    return top_scor


def score_comp(g_s, f):  # Счётчик очков игрока

    g_s.point_y += g_s.rif_speed*g_s.kof
    t_score = f.render("Овечки: "+str(g_s.score), 1, (95, 0, 144))
    return t_score


def rif_spawn(screen, surf, g_s, rifs):  # Спаун рифов
    surf.fill(g_s.screen_color)
    screen.blit(surf, (10, g_s.point_y))
    g_s.point_score += g_s.rif_speed*g_s.kof
    if g_s.point_y >= 150:  # Условие спавна рифов
        g_s.point_y = 0
        rifs_spawn(screen, rifs, g_s)


def rifs_spawn(screen, rifs, g_settings):  # генерация рифов
    rif = Rif(randrange(0, g_settings.screen_wigth, 10), 0, screen, rifs, g_settings)
    rif_wigth = rif.get_rif_wigth()
    buf = rif.get_rif_wigth() * 5  # Расстояние между рифами по горизонтали
    position = 0
    rand_y = -50
    while g_settings.screen_wigth > position + rif_wigth * 2:
        position += buf
        shans = randrange(1, 100)  # Шанс спавна рифа
        shans_2 = randrange(40, 60)  # Шанс необходимый шанс для спавна рифа
        rand_div_y = randrange(-30, 30, 10)  # Отколонение по Y

        if shans < shans_2:
            num_rifs = randrange(1, 3)
            for i in range(0, num_rifs):
                coin_c = randrange(1, 100)  # Шанс спавна овцы
                if coin_c < 20:
                    g_settings.coin = True
                else:
                    g_settings.coin = False
                Rif(position, rand_y + rand_div_y, screen, rifs, g_settings)
                position += rif_wigth
        else:
            position += rif_wigth + buf


def cleaning(g_s):  # Сброс положения корабля и паруса после поражения
    g_s.menu_flag = True
    g_s.score = 0
    g_s.ship_cord = 1366 / 2  # Центровка корабля по центру экрана после смерти
    g_s.ship_speed = 0  # Горизонтальная скорость

    g_s.i = 1
    g_s.j = 1
    g_s.w = 2


def collied_rifs(ship, rifs, g_s, players):  # Столкновение корабля и рифа
    for rect_rif in rifs:
        if ship.rect.colliderect(rect_rif):
            if rect_rif.coin:
                rifs.remove(rect_rif)
                g_s.score += 1  # Начисление очков за монету
            else:
                score_save(g_s, players)
                cleaning(g_s,)
                ship.sc_up(1, 1)
                ship.blit()
                all_rif_remove(rifs)


def all_rif_remove(rifs):  # отчистка коллекции с рифами после смерти
    for rif in rifs:
        rifs.remove(rif)


def speed_up(g_s, ship):  # Обновление скорости корабля
    g_s.rif_speed, g_s.ship_speed = ship.s_l[g_s.w][g_s.i][g_s.j]

# def speed_up(g_s, ship):  # Обновление скорости корабля
#
# ##### НЕОБХИДИМО ДОБАВИТЬ УСКОРЕНИЕ!!!!!
#         g_s.rif_speed, g_s.ship_speed = ship.s_l[g_s.w][g_s.i][g_s.j]
#         # g_s.rif_speed, g_s.ship_speed = ship.s_l[2][1][1]
#
#         a = g_s.rif_speed/10
#
#         if g_s.rif_speed <= 0.25 or g_s.rif_speed == 0:
#             g_s.V_speed -= a
#             print(g_s.V_speed)
#         if g_s.rif_speed > 0.25 and g_s.V_speed < 2:
#             g_s.V_speed += a

def skin_load(event, g_settings, ship):  # Управление Скином

    if event.key == pygame.K_a:
        if g_settings.i != 0:
            g_settings.i -= 1
        ship.sc_up(g_settings.i, g_settings.j)

    if event.key == pygame.K_d:
        if g_settings.i != 2:
            g_settings.i += 1
        ship.sc_up(g_settings.i, g_settings.j)

    if event.key == pygame.K_LEFT:
        if g_settings.j != 0:
            g_settings.j -= 1
        ship.sc_up(g_settings.i, g_settings.j)

    if event.key == pygame.K_RIGHT:
        if g_settings.j != 2:
            g_settings.j += 1
        ship.sc_up(g_settings.i, g_settings.j)


def ship_skin_set(g_settings, buttons, mouse_x, mouse_y, ship):  # Уствновка цвета паруса в настройках игры
    if buttons[0].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'red_ship'
        g_settings.bk_color = 'red_bk'
        g_settings.color_path = 'red'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[1].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'yellow_ship'
        g_settings.bk_color = 'yellow_bk'
        g_settings.color_path = 'yellow'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[2].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'green_ship'
        g_settings.bk_color = 'green_bk'
        g_settings.color_path = 'green'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[3].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'black_ship'
        g_settings.bk_color = 'black_bk'
        g_settings.color_path = 'black'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    ship.ship_skin_load(g_settings.color_path)
    ship.sc_up(1, 1)


def check_play_button(rifs, g_settings, buttons, mouse_x, mouse_y, players, screen, ship):  # Проверка нажатия клафиш в меню
    if buttons[0].rect.collidepoint(mouse_x, mouse_y):  # Загрузка меню

        if not g_settings.game_active and not g_settings.menu_flag:
            g_settings.game_active = True
            g_settings.pause_flag = False

        else:
            g_settings.menu_flag = False
            g_settings.game_active = True

            # if g_settings.new_game_intro:  # Загрузка интро когда игрок заходит в игру первый раз
            #     n_g_intro = New_game_intro(g_settings, screen)
            #     n_g_intro.intro_load()
            #     g_settings.new_game_intro = False

            pygame.mixer.music.stop()
            menu_music('ship_song', g_settings)

    elif buttons[3].rect.collidepoint(mouse_x, mouse_y):  # Нажата клавиша выход
        if g_settings.pause_flag:
            g_settings.menu_flag = True
            g_settings.pause_flag = False
            score_save(g_settings, players)
            all_rif_remove(rifs)  # Отчистка коллекции рифов
            g_settings.score = 0
            cleaning(g_settings)  # перемещенеи корабля на исходную позицию

        elif g_settings.menu_flag:
            score_save(g_settings, players)
            g_settings.menu_flag = False
            g_settings.ALL_game = False


    elif buttons[2].rect.collidepoint(mouse_x, mouse_y) and g_settings.menu_flag:  # Рекорды
        g_settings.menu_flag = False
        g_settings.p_record_flag = True

        rec_board = Records(g_settings, screen)
        rec_board.set_load()

    elif buttons[1].rect.collidepoint(mouse_x, mouse_y) and g_settings.menu_flag:  # Настройки
        g_settings.menu_flag = False
        g_settings.g_settings_flag = True

        g_s = GameSettings(g_settings, screen, ship)
        g_s.g_set_load()


def pause_start(event, g_settings):  # Игровая пауза
    if event.key == pygame.K_ESCAPE:
        if g_settings.game_active:
            g_settings.pause_flag = True
            g_settings.game_active = False
        else:
            g_settings.pause_flag = False
            g_settings.game_active = True


def check_event(g_settings, wind_rose, ship, players):  # Проверка всех игровых событий

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score_save(g_settings, players)
            g_settings.ALL_game = False

        elif event.type == pygame.KEYDOWN:
            skin_load(event, g_settings, ship)
            pause_start(event, g_settings)
            if event.key == pygame.K_LALT and event.key == pygame.K_F4:
                g_settings.game_active = False
                g_settings.menu_flag = False
                g_settings.ALL_game = False

        elif event.type == pygame.USEREVENT:
            wind_rose_time(g_settings, wind_rose)


def screen_up(screen, g_settings, rifs, ship, t_score, top_scor):  # Отрисовка экрана
    screen.fill(g_settings.screen_color)
    speed_up(g_settings, ship)
    rifs.update(g_settings.screen_height, g_settings.rif_speed)
    rifs.draw(screen)
    screen.blit(top_scor, (25, 25))
    screen.blit(t_score, (g_settings.screen_wigth - 200, 25))
