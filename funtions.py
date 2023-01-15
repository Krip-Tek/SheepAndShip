import pygame
import json
from random import *
import math
from rif import Rif
from game_settings import GameSettings
from records import Records
from new_game_intro import New_game_intro


def menu_music(sound_name, g_settings):  # Звуковое сопровождение
    pygame.mixer.music.load(f'sounds/{sound_name}.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(g_settings.music_volume)


def rand_time_rotate():  # Случайный выбор через сколько изменится направление ветра
    time_r = randrange(10, 25 + 1)
    return time_r


def ship_rotate(g_s, ship):  # Вращение корабля
    image, rect = ship.rotate_ship(ship.image, g_s.ship_angle)
    if g_s.ship_rotate_left and g_s.ship_angle > -90:
        g_s.ship_angle -= 1 % 360
        g_s.sail_angle -= 1 % 360
    if g_s.ship_rotate_right and g_s.ship_angle < 90:
        g_s.ship_angle += 1 % 360
        g_s.sail_angle += 1 % 360
    return image, rect


def sail_rotate(g_s, sail):  # Вращение паруса
    image, rect = sail.rotate_sail(sail.image, g_s.sail_angle)
    if g_s.sail_rotate_left and g_s.sail_angle > g_s.ship_angle - 90:
        g_s.sail_angle -= 1.5 % 360
    if g_s.sail_rotate_right and g_s.sail_angle < g_s.ship_angle + 90:
        g_s.sail_angle += 1.5 % 360
    return image, rect


def wind_rose_time(g_s, w_r):  # Поворот розы ветров
    image, rect = w_r.rotate_wind_rose(w_r.image, g_s.wind_rose_angle)

    if g_s.basic_wing_angle > g_s.wind_rose_angle and g_s.wind_rose_angle < 90:
        g_s.wind_rose_angle += 0.25 % 360
    elif g_s.basic_wing_angle < g_s.wind_rose_angle and g_s.wind_rose_angle > -90:
        g_s.wind_rose_angle -= 0.25 % 360
    else:
        g_s.basic_wing_angle += randrange(-3, 3)  # Флуктуации ветра
        pass

    return image, rect


def score_save(g_s, players):  # Сохранение счёта игрока
    if g_s.score > int(g_s.top_score):
        g_s.top_score = g_s.score
        players[g_s.name_in] = g_s.top_score
    with open("records.json", "w") as file:
        json.dump(players, file, indent=4, ensure_ascii=False)


def top_score(g_s, f):
    top_scor = f.render("Рекорд: " + str(g_s.top_score), 1, (95, 0, 144))
    return top_scor


def score_comp(g_s, f):  # Счётчик очков игрока
    g_s.point_y += g_s.rif_speed * g_s.kof
    t_score = f.render("Овечки: " + str(g_s.score), 1, (95, 0, 144))
    return t_score


def rif_spawn(screen, surf, g_s, rifs):  # Спаун рифов
    surf.fill(g_s.screen_color)
    screen.blit(surf, (10, g_s.point_y))
    g_s.point_score += g_s.rif_speed * g_s.kof
    if g_s.point_y >= 150:  # Условие спавна рифов
        g_s.point_y = 0
        rifs_spawn(screen, rifs, g_s)


def rifs_spawn(screen, rifs, g_settings):  # генерация рифов
    rif = Rif(randrange(0, g_settings.screen_width, 10), 0, screen, rifs, g_settings)
    rif_wigth = rif.get_rif_wigth()
    buf = rif.get_rif_wigth() * 5  # Расстояние между рифами по горизонтали
    position = 0
    rand_y = -50
    while g_settings.screen_width > position + rif_wigth * 2:
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


def collied_rifs(ship, rifs, g_s, players):  # Столкновение корабля и рифа
    for rect_rif in rifs:
        if ship.rect.colliderect(rect_rif):
            if rect_rif.coin:
                rifs.remove(rect_rif)
                g_s.score += 1  # Начисление очков за монету
            else:  # Столкновение крабля с рифом
                score_save(g_s, players)
                cleaning(g_s,)
                ship.sc_up(1, 1)
                ship.blit()
                all_rif_remove(rifs)


def all_rif_remove(rifs):  # отчистка коллекции с рифами после смерти
    for rif in rifs:
        rifs.remove(rif)


def ship_skin_set(g_settings, buttons, mouse_x, mouse_y, ship, sail):  # Уствновка цвета паруса в настройках игры
    if buttons[0].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'red_ship'
        g_settings.bk_color = 'red_bk'
        g_settings.color_name = 'red_sail'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[1].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'yellow_ship'
        g_settings.bk_color = 'yellow_bk'
        g_settings.color_name = 'yellow_sail'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[2].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'green_ship'
        g_settings.bk_color = 'green_bk'
        g_settings.color_name = 'green_sail'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    if buttons[3].rect.collidepoint(mouse_x, mouse_y):
        g_settings.skin_color = 'black_ship'
        g_settings.bk_color = 'black_bk'
        g_settings.color_name = 'black_sail'

        g_settings.g_settings_flag = False
        g_settings.menu_flag = True

    sail.sail_skin_load(g_settings.color_name)


def check_play_button(rifs, g_settings, buttons, mouse_x, mouse_y, players, screen,
                      ship, sail):  # Проверка нажатия клафиш в меню
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
            g_settings.rif_speed = 0
            g_settings.ship_speed = 0
            g_settings.ship_angle = 0
            g_settings.sail_angle = 0
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

        g_s = GameSettings(g_settings, screen, ship, sail)
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
            # Включение флагов на поворот корабля
            if event.key == pygame.K_a:
                g_settings.ship_rotate_left = True
            if event.key == pygame.K_d:
                g_settings.ship_rotate_right = True
            # Включение флагов на поворот паруса
            if event.key == pygame.K_j:
                g_settings.sail_rotate_left = True
            if event.key == pygame.K_l:
                g_settings.sail_rotate_right = True

            pause_start(event, g_settings)
            if event.key == pygame.K_LALT and event.key == pygame.K_F4:
                g_settings.game_active = False
                g_settings.menu_flag = False
                g_settings.ALL_game = False

        elif event.type == pygame.KEYUP:
            # Выключение флагов на поворот корабля
            if event.key == pygame.K_a:
                g_settings.ship_rotate_left = False
            if event.key == pygame.K_d:
                g_settings.ship_rotate_right = False

            # Выключение флагов на поворот паруса
            if event.key == pygame.K_j:
                g_settings.sail_rotate_left = False
            if event.key == pygame.K_l:
                g_settings.sail_rotate_right = False

        elif event.type == pygame.USEREVENT:
            # Углы на которые поворачивается основа направления ветра
            g_settings.basic_wing_angle = (randrange(-90, 91, 15))
            # Перерасчет времени нового события (через сколько)
            pygame.time.set_timer(pygame.USEREVENT, (1000 * rand_time_rotate()))


def ship_move_force(g_s):
    g_s.sail_force = g_s.wind_force*(math.cos(math.radians(g_s.wind_rose_angle) - math.radians(g_s.sail_angle)))
    if g_s.sail_force <= 0:
        g_s.sail_force = 0
    g_s.ship_force_x = g_s.sail_force * (math.cos(math.radians(g_s.ship_angle)))
    g_s.ship_force_y = g_s.sail_force * (math.sin(math.radians(g_s.ship_angle)))


def speed_up(g_s):
    # вертикальная составляющая
    g_s.max_speed_x = g_s.ship_force_x*g_s.All_speed_kof

    if g_s.ship_force_x > 0 and g_s.rif_speed < g_s.max_speed_x:
        g_s.rif_speed += g_s.ship_force_x / g_s.All_speed_kof

    elif g_s.rif_speed > g_s.min_speed_x:
        g_s.rif_speed -= g_s.stop_force  # Сила торможения
        if g_s.rif_speed <= 0:
            g_s.rif_speed = 0

    # горизонтатьная составляющая
    g_s.max_speed_y = g_s.ship_force_y * g_s.All_speed_kof

    if g_s.ship_force_y != 0 and g_s.ship_speed < math.fabs(g_s.max_speed_y):
        g_s.ship_speed += math.fabs(g_s.ship_force_y) / g_s.All_speed_kof

    elif math.fabs(g_s.ship_force_y) == 0 and g_s.ship_speed != 0:
        g_s.ship_speed -= g_s.stop_force  # Сила торможения
        if g_s.ship_speed <= 0:
            g_s.ship_speed = 0


def screen_up(screen, g_settings, rifs, ship, t_score, top_scor, sail):  # Отрисовка экрана
    screen.fill(g_settings.screen_color)
    ship_move_force(g_settings)

    speed_up(g_settings)
    rifs.update(g_settings)
    ship.update(g_settings)
    sail.move_sail(ship)

    rifs.draw(screen)
    screen.blit(top_scor, (25, 25))
    screen.blit(t_score, (g_settings.screen_width - 200, 25))
