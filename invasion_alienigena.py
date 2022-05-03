import sys
from turtle import bgcolor

import pygame
from configuraciones import Configuraciones
def run_game():
    #inicializar el jueego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion Alienigena")
    

    #iniciar el bucle principal del juego

    while True:

        #escuchar eventos de teclado o de raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # volver a dibujar la pantalla durante cada psada por el bucle        
        pantalla.fill(ai_configuraciones.bg_color)

        #hacer visible la pantalla dibujanda mas reciente        
        pygame.display.flip()
run_game()        
