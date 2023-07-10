import pygame

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game): # получаем два параметра: ссылку self и ссылку на текущий экземпляр класса AlienInvasion
        #так класс ship получает доступ ко всем игровым ресурсам.
        self.screen = ai_game.screen # экран присваивается атрибуту Ship ,что бы к нему можно было обращаться во
        # всех модулях класса
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #класс Rect и метод get_rect позволяет расположить корабль в нужной позиции
        self.image = pygame.image.load('images/ship.bmp') #загружаем изображение,функция представляет поверхность self.image
        self.rect = self.image.get_rect() # когда изображение будет загружено,программа вызовет get_rect()
        #для получения атрибута rect поверхности корабля,что бы позднее ипользовать ее для позиционирования корабля
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom # midbottom указывает что корабль будет находиться по середине
        #внизу

        #Сохранения вещественной координаты центра коробля.
        self.x = float(self.rect.x)

        #Флаг перемещения
        self.moving_right = False # в неподвижном состояние корабля moving_right равен False,при нажатии
        # клавиши вправо,флагу присваивается значении True,когда будет отпущена обратно заначение False
        self.moving_left = False

    def update(self):# метода update изменяет позицию корабля если флаг содержит значение True,метод будет вызываться каждый раз когда вы хотите обновить позицию корабля
        #Обновляет позицию корабля с учетом флагов
        #Обновляем атрибут x,не rect
        if self.moving_right and self.rect.right < self.screen_rect.right: #  выставление границ справа
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  #  выставление границ слева
            self.rect.x -= self.settings.ship_speed


    def blitme(self): #метод выводит изображение на экран в позиции заданной self.rect
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image,self.rect)
