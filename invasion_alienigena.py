import imp
from turtle import bgcolor

import pygame
import funciones_juego as fj
from configuraciones import Configuraciones
from nave import Nave

def run_game():
    #inicializar el jueego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion Alienigena")
    
    #crea nave
    nave = Nave(ai_configuraciones, pantalla)

    #iniciar el bucle principal del juego

    while True:

        #escuchar eventos de teclado o de raton
        fj.verificar_eventos(nave)
        nave.update()
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave)
run_game()        
