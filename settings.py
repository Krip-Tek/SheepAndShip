class Settings:
    """Параметры игры"""
    def __init__(self):
        self.screen_width = 1366  # Ширина экрана
        self.screen_height = 768  # Высота экрана
        self.screen_color = (1, 140, 233)  # Цвет экрана

        self.ALL_game = True
        self.All_speed_kof = 3
        self.stop_force = 0.005

        self.FPS = 60  # Частота кадров

        self.ship_speed = 0  # Горизонтальная скорость
        self.max_speed_x = 0
        self.min_speed_x = 0

        self.ship_cord = 0

        self.max_speed_y = 0
        self.min_speed_y = 0
        self.basic_ship_speed = 0

        self.rif_speed = 0  # Вертикальная скороcть
        self.basic_rid_speed = 0

        self.ship_angle = 0  # Угол поворота корабля

        self.sail_angle = 0  # Угол поворота паруса

        self.wind_rose_angle = 0  # Угол поворота Розы Ветров
        self.basic_wing_angle = 0  # Базовый угол поворота Розы Ветров

        self.top_score = 0
        self.score = 0  # Очки игрока
        self.music_volume = 0  # Громкость музыки от 0 до 1

        self.wind_force = 1  # сила ветра
        self.sail_force = 0  # сила паруса
        self.ship_force_x = 0  # сила корабля по X
        self.ship_force_y = 0  # сила корабля по Y

        self.kof = 1  # Значение коэффициента увеличивающего скороcть игры

        self.rif_spawn_time = 5  # Время очередного спавна рифов

        self.point_y = 0  # Условная координата спавна рифов
        self.coin = False
        self.point_score = 0

        self.name_in = ""

        self.game_active = False

        self.menu_flag = True
        self.pause_flag = False
        self.g_settings_flag = False
        self.p_record_flag = False

        # установка цветов корабля и фона
        self.skin_color = 'red_ship'
        self.bk_color = 'red_bk'

        self.intro_flag = 1
        self.alpha_flag = 1
        self.alpha = 1

        self.new_game_intro = True

        # Флаги управления поворота кораблем
        self.ship_rotate_left = False
        self.ship_rotate_right = False

        # Флаги управления поворота паруса
        self.sail_rotate_left = False
        self.sail_rotate_right = False
