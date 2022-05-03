import pygame

class Nave():
    #Sirve para gestionar el comportamiento de la nave

    def __init__(self, pantalla):
        #inicializa la nave y establece su posicion de partida
        self.pantalla = pantalla

        #cargar la imagen de la nave y ontiene su rect
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #empieza cada nueva nace en la parte inferior central de la pantalla

        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
    def blitme(self):
        #dibuja la nave en su ubicacion actual
        self.pantalla.blit(self.imagen, self.rect)    