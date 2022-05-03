import sys
from turtle import bgcolor

import pygame

def run_game():
    #inicializar el jueego y crear un objeto en pantalla
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Invacion Alienigena")
    #Color de fondo
    bg_color = (230, 230, 230) 

    #iniciar el bucle principal del juego

    while True:

        #escuchar eventos de teclado o de raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # volver a dibujar la pantalla durante cada psada por el bucle        
        pantalla.fill(bg_color)

        #hacer visible la pantalla dibujanda mas reciente        
        pygame.display.flip()
run_game()        
