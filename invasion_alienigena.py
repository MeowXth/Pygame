import sys

import pygame

def run_game():
    #inicializar el jeugo y crear un objeto en pantalla
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Invacion Alienigena")
    #iniciar el bucle principal del juego
    while True:

        #escuchar eventos de teclado o de raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #hacer visible la pantalla dibujanda mas reciente        
        pygame.display.flip()
run_game()        
