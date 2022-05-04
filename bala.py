from cmath import rect
import imp
import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    #sirve para manejar las balas disparadas desde la nave 
    def __init__(self, ai_configuraciones, pantalla, nave):

        super(Bala, self).__init__()
        self.pantalla = pantalla
        #crea una bala rect en (0,0) y luego establece la posicion correcta
        self.rect = pygame.Rect(0, 0, ai_configuraciones.bala_width, ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        #almacena la posicon de la bala como un valor decimal
        self.y = float(self.rect.y)
        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad

    def update(self):
        #mueve la bala hacia la pantalla
        #actualiza la posicon decimal de la bala
        self.y -= self.factor_velocidad
        #Actualiza la poscion del rect
        self.rect.y = self.y

    def draw_bala(self):
        #dibuja la bala en la pantalla
        pygame.draw.rect(self.pantalla, self.color, self.rect)    

