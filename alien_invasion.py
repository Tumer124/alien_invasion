import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.settings = Settings() #создаем экземпляр который принимает настройки из файла settings и
        #класса Setting

        """#Полноэкранный режим
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_widht = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height"""

        self.screen = pygame.display.set_mode((self.settings.screen_widht,self.settings.screen_height)) #создает окно в котором,в котором прорисовываются
        #все графические элементы игры,
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # группа для прорисовки снарядов на экране

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events() # Отслеживание событий клавиатуры и мыши.
            self.ship.update() #позиция коробля будет обновляться после проверки событий клавиатуры,
            # но перед обновлением экрана
            self._update_bullets() #Обновляет позиции снарядов и уничтожает старые снаряды
            self._update_screen() # Обновляет изображение на экране и отображает новый экран




    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():  # метод(обработчик событий,при любом событии клавиатуры или мыши
            # отрабатывает цикл for
            if event.type == pygame.QUIT:  # например когда человек кликает по кнопке закрытие игрового окна
                # программа обнаруживает событие pygame.QUIT и вызывает метод sys.exit для выхода из игры
                sys.exit()
            elif event.type == pygame.KEYDOWN: # каждое нажатие клавиши регестрируется как событие KEYDOWN
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: # когда отпущена клавиша
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:  # проверяет через обработчик была ли нажата именно эта клавиша
            # переместить корабль вправо.
            self.ship.moving_right = True  # пока нажата клавиша вправо то корабль перемещается
        elif event.key == pygame.K_LEFT:  # проверяет через обработчик была ли нажата именно эта клавиша
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:  # когда отпущена клавиша впрво
            self.ship.moving_right = False  # то корабль останавливается
        elif event.key == pygame.K_LEFT:  # когда отпущена клавиша
            self.ship.moving_left = False

    def _fire_bullet(self):
        #"""Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed: # указываем ,что на экране может быть не больше трех снарядов
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #Обновляет позиции снарядов и уничтожает старые снаряды
        self.bullets.update()  # вызов update() для группы приводит к автоматическому вызову update()
        # для каждого спрайта в группе. Строка self.bullets.update() вызывает bullet.update() для каждого снаряда ,включенного в группу bullets

        # Удаление снарядов,вышедших за край экрана
        for bullet in self.bullets.copy():  # метод copy используется для создания цикла for в котором можно изменить содержимое bullets
            if bullet.rect.bottom <= 0:  # программа проверяет каждый снаряд и определяет вышел ли он за верхний край экрана
                self.bullets.remove(bullet)  # если пересек границу,он удаляется из bullets
        print(len(self.bullets))


    def _update_screen(self):
         #Обновляет изображение на экране и отображает новый экран.

        self.screen.fill(self.settings.bg_color)  # применяем цвет фона через метод fill,получивший один аргумент
        # цвет фона

        self.ship.blitme() # после заполнения фона корабль рисуется на экране вызовом ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()