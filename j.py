import pygame #импортируем код в pygame
from random import *

class Sprites():#создание класса
    def __init__(self,a,b,c):#создание конструктора, в нем создается свойства,он вызывается при создании объекта
        self.img = pygame.image.load(a)#создание картинки,ЭТО СВОЙСТВО



        self.rect = self.img.get_rect()# получение прямоугольника от картинки,ЭТО СВОЙСТО
        self.rect.x = b#создание координат,ЭТО СВОЙСТВО
        self.rect.y = c#создание координат,ЭТО СВОЙСТВО

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def move_food(self):
        self.rect.y += 5

    def move_plate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

y4=randint(-500,0)
y2=randint(-500,0)
y=randint(-500,0)
monster1= Sprites("монстр.png",250,y4)
monster2= Sprites("монстр.png",400,y4)
monster4 = Sprites("монстр.png",200,y4)
monster2 = Sprites("монстр.png",350, y)
monster1 = Sprites("монстр.png",500,y2)

monster_list = [monster1, monster2, monster4]
fon = Sprites('комнота.jpg', 0, 0)# создание фона
main_sprite = Sprites('мамин кашелёк.png', 450, 390)# создание фона
pygame.init()#обезательная программа
window_size=(930,495)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
clock = pygame.time.Clock() #фпс


while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу klassa Food (фон)
    main_sprite.draw_image() #приминение метода отрисовки картинки к объкеу klassa Food (тарелка)
    main_sprite.move_plate()# применение метода к объкту
    clock.tick(40)#40фпс
    for i in monster_list:
        i.draw_image()
        i.move_food()
        if i.rect.y>700:
            i.rect.y = 0

        if main_sprite.rect.colliderect(i.rect):
            monster_list.remove(i)
        if monster_list == []:
            pygame.QUIT()
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()# выход из игры
    pygame.display.update()  # обновление содержимого экрана
