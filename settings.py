class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25,25,112)

        # Настройки корабля
        self.ship_speed = 1

        # Параметры стрельбы
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 153)
        self.bullet_allowed = 2

        # Настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # self_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1