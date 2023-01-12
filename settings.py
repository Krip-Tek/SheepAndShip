class Settings:
    """Параметры игры"""

    def __init__(self):
        self.screen_wigth = 1366  # Ширина экрана
        self.screen_height = 768  # Высота экрана
        self.screen_color = (1, 140, 233)  # Цвет экрана

        self.FPS = 60  # Частота кадров
        self.ship_cord = 0
        self.ship_speed = 0  # Горизонтальная скорость
        self.ship_angle = 0  # Угол поворота корабля
        self.sail_angle = 0  # Угол поворота паруса
        self.top_score = 0
        self.score = 0  # Очки игрока

        self.i = 1
        self.j = 1
        self.w = 2
        self.color_path = 'red' # Папка со скинами кораблей

        self.kof = 10  # Значение коэффициента увеличивающего скороcть игры
        self.rif_speed = 1  # Вертикальная скороcть
        self.rif_step = 0  #
        self.rif_second = 1  #

        self.wind_rose_step = 0  #
        self.wind_rose_second = 0  #
        self.wind_rose_angle = 0  # Угол поворота Розы Ветров

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
        self.skin_color  = 'red_ship'
        self.bk_color = 'red_bk'


        self.intro_flag = 1
        self.alpha_flag = 1
        self.alpha = 1

        self.new_game_intro = True

        self.ALL_game = True
