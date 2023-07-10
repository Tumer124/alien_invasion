import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""

    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__() # метод для наследования от класса Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Создание снаряда в позиции (0,0) и назначение правильной позиции.

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height) # создаем экземпляр класса прямоугольника с местоположениембшириной и высотой
        self.rect.midtop = ai_game.ship.rect.midtop # атрибуту midtop снаряда присваивается значение midtop корабля.Снаряд должен
        #появляться у верхнего края корабля,поэтому верхний край снаряда совмещается с вверхним краем прямоугольника корабля
        #для имитации выстрела из корабля

        #Позиция снаряда хранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self): # метод управляет позицией снаряда
        """Перемещает снаряд вверх по экрану."""
        #Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed # Когда происходит выстрел,снаряд двигается вверх по экрану,
        #что соответствует уменьшению координаты y,следовательно для обновления позиции снаряда,следует
        #вычесть велечину,хранящуюся в settings.bullet_speed из self.y
        #Обновление позиции прямоугольника.
        self.rect.y = self.y # Затем значение self.y используется для изменеия значения self.rect.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen,self.color,self.rect)