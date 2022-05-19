import imp
from turtle import bgcolor

import pygame
from pygame.sprite import Group
import funciones_juego as fj
from configuraciones import Configuraciones
from nave import Nave
from button import Button
from estadisticas import Estadisticas

def run_game():
    #inicializar el jueego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion Alienigena")
    #crea el boton play 
    play_button = Button(ai_configuraciones, pantalla,  "Play")


    #Crea una instancia para almacenar estadisticas del juego
    estadisticas = Estadisticas(ai_configuraciones)
    
    #crea nave,#crea un grupo para almacenar las balas,grupo de alien
    nave = Nave(ai_configuraciones, pantalla)
    balas = Group()
    aliens = Group()
    #crea la flota de  aliens
    fj.crear_flota(ai_configuraciones,pantalla,nave,aliens)
    #iniciar el bucle principal del juego

    while True:

        #escuchar eventos de teclado o de raton
        fj.verificar_eventos(ai_configuraciones, pantalla,estadisticas, play_button, nave,aliens, balas)
        if estadisticas.game_active:
            nave.update()
            fj.update_balas(ai_configuraciones, pantalla,nave,balas,aliens)
            fj.update_aliens(ai_configuraciones,estadisticas, pantalla ,nave, aliens, balas)
                
        fj.actualizar_pantalla(ai_configuraciones, pantalla,estadisticas, nave, aliens, balas, play_button)
run_game()        
