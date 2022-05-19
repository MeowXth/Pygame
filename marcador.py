from importlib.metadata import SelectableGroups
import pygame
from pygame.sprite import Group
from nave import Nave

class Marcador():
    """Una clase para reportar informacion sobre puntuacion"""
    def __init__(self, ai_configuraciones, pantalla, estadisticas):
        """Inicializa los atributos de registro de puntajes"""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        self.ai_configuraciones = ai_configuraciones
        self.estadisticas = estadisticas

        #Ajustes de fuente para la inforacion de puntuacion
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #Prerara la imagen del puntuaje inicial
        self.prep_puntaje()
        self.prep_alto_puntaje()
        self.prep_nivel()
        self.prep_naves()

    def prep_puntaje(self):
        """Convierte el marcador en una imagen renderizada"""
        puntaje_redondeador = int (round(self.estadisticas.puntaje, -1))
        puntaje_str = "{:,}".format(puntaje_redondeador)
        self.puntaje_imagen = self.font.render(puntaje_str, True, self.text_color, self.ai_configuraciones.bg_color)

        #muestra el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_imagen.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20

    def muestra_puntaje(self):
        """Dibuja la puntuacion en la pantalla"""
        self.pantalla.blit(self.puntaje_imagen, self.puntaje_rect)
        self.pantalla.blit(self.alto_puntaje_imagen, self.alto_puntaje_rect)
        self.pantalla.blit(self.nivel_imagen, self.nivel_rect)
        #Dibuja las naves
        self.naves.draw(self.pantalla)


    def prep_alto_puntaje(self):
        """Convierte el marcador en una imagen renderizada"""
        puntaje_alto = int (round(self.estadisticas.alto_puntaje, -1))
        alto_puntaje_str = "{:,}".format(puntaje_alto)
        self.alto_puntaje_imagen = self.font.render(alto_puntaje_str, True, self.text_color, self.ai_configuraciones.bg_color)

        #centra el puntaje mas alto en la parte superior de la pantalla
        self.alto_puntaje_rect = self.alto_puntaje_imagen.get_rect()
        self.alto_puntaje_rect.centerx = self.pantalla_rect.centerx
        self.alto_puntaje_rect.top = self.puntaje_rect.top
    
    def prep_nivel(self):
        """Convierte el nivel en una imagen renderizada"""
        self.nivel_imagen = self.font.render(str(self.estadisticas.nivel), True,self.text_color, self.ai_configuraciones.bg_color)

        #posiciona el nivel debajo del puntaje

        self.nivel_rect = self.nivel_imagen.get_rect()
        self.nivel_rect.right = self.pantalla_rect.right - 20
        self.nivel_rect.top = self.puntaje_rect.bottom + 10

    def prep_naves(self):
        """Muestra cuantas naves quedan"""
        self.naves = Group()
        for numero_nave in range(self.estadisticas.naves_restantes):
            nave = Nave(self.ai_configuraciones, self.pantalla)
            nave.rect.x = 10 + numero_nave * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)    