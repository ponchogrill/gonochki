import pygame as pg
import sys
from car import Car
from grass import Grass

FPS = 60
W = 800
H = 1000
WHITE = (255, 255, 255)
sc = pg.display.set_mode((W, H))
clock = pg.time.Clock() 
# координата x будет случайна
car1 = Car(x = (W - 200) // 2, y = (W - 200) // 2)
grass1 = Grass('grass.png', sc, (W - 200) // 2, 0)
grass2 = Grass('grass.png', sc, (W - 200) // 2, - H)
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    sc.fill(WHITE)
    sc.blit(grass.image, grass.rect)
    sc.blit(car1.image, car1.rect)
    grass.update()
    car1.update()
    pg.display.flip
    clock.tick(FPS)
    pg.display.update()
