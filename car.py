import pygame as pg
W = 800
H = 1000
class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image,(50, 80))
        self.surf = pg.image.load('car1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = W // 2
        self.rect.bottom = H - 10
        self.x = car1
    def update(self):
        keys = pg.key.get_pressed()
        #если нажата
        if keys[pg.K_RIGHT]:
            self.rect_x = 10
            self.x += self.rect_x
        #если нажата
        if keys[pg.K_LEFT]:
            self.rect_x = -10
            self.x += self.rect_x
            
        
