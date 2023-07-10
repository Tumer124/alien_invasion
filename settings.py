
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        "Инициализируем настройки игры"
        #Параметры экрана
        self.screen_widht = 1200 # ширина
        self.screen_height = 800 # длинна
        self.bg_color = (230, 230, 230) # цвет фона

        # Настройки корабля
        self.ship_speed = 1.5 # скорость корабля(атрибут определяет велечину смещения при каждом проходе цикла )

        #Параметры снаряда
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed =3 # максимально допустимое количество снарядов