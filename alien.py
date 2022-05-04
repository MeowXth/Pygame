import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_configuraciones, pantalla):
        super(Alien, self).__init__()

        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        #carga la imagen del alien y establece su atributo rect
        self.image = pygame.image.load("imagenes/alien.bmp")
        self.rect = self.image.get_rect()
        #inicia en la parte superior izquierda de la pantalla

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #almacena la posicion exacta del alien

        self.x = float(self.rect.x)

    def blitme(self):
        #dibuja al alien en su ubicacion actual
        self.pantalla.blit(self.image, self.rect)
