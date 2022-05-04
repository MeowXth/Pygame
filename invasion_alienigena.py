import imp
from turtle import bgcolor

import pygame
from pygame.sprite import Group
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
    #crea un grupo para almacenar las balas
    balas = Group()
    #iniciar el bucle principal del juego

    while True:

        #escuchar eventos de teclado o de raton
        fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
        
        nave.update()
        fj.update_balas(balas)
                
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, balas)
run_game()        
