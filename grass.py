import pygame as pg
W = 800
H = 1000
class Grass(pg.sprite.Sprite):
    def __init__(self, filename, screen, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image,(800, 1000))
        self.surf = pg.image.load('grass.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
    def update(self):
        pass
    def draw(self):
        self.screen_blit(self.image, self.rect)
