import sys
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

    def move_money(self): #движение монет
        self.rect.y += 5

    def move_plate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5



money1 = Sprites("монстр.png", randint(0,900), randint(-500,0))
money2 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money3 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money4 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money5 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money6 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money7 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money8 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money9 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money10 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money11 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money12 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money13 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money14 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money15 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money16 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money17 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money18 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money19 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money20 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money21 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money22 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money23 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money24 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money25 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money26 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money27 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money28 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money29 = Sprites("монстр.png",randint(0,900), randint(-500,0))
money30 = Sprites("монстр.png",randint(0,900), randint(-500,0))

money_list = [money1, money2, money3, money4, money5, money6, money7, money8, money9, money10, money11, money12, money13, money14, money15, money16, money17, money18, money19, money20, money21, money22, money23, money24, money25, money26, money27, money28, money29, money30,]
fon = Sprites('комнота.jpg', 0, 0)# создание фона
main_sprite = Sprites('мамин кашелёк.png', 450, 390)# создание фона
pygame.init()#обезательная программа
window_size=(930,495)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
clock = pygame.time.Clock() #фпс
font = pygame.font.SysFont("Arial",30) #создание шрифта
count = 0


while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу klassa Food (фон)
    text = font.render("счёт "+str(count), True, (255, 255, 255))  # создание текста
    screen.blit(text, (50, 50))  # отрисовка текста
    main_sprite.draw_image() #приминение метода отрисовки картинки к объкеу klassa
    main_sprite.move_plate()# применение метода к объкту
    clock.tick(40)#40фпс
    for i in money_list:
        i.draw_image()
        i.move_money()
        if i.rect.y>700:
            i.rect.y = 0

        if main_sprite.rect.colliderect(i.rect): #если кошелёк коснулся монеты
            money_list.remove(i) #удалить монету из списка монет
            count += 1 #увеличеть переменную count на 1

        if money_list == []: #если список монет пустой
            sys.exit() #выход из игры
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
            sys.exit() # выход из игры
    pygame.display.update()  # обновление содержимого экрана
