import sys
import pygame

from nave import Nave

def verificar_eventos(nave):
    #responde a las pulsaciones de teclas y los eventos del raton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = False           
def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    #actualiza las imagens en la pantalla y pasa a la nueva pantalla
    # volver a dibujar la pantalla durante cada psada por el bucle        
    pantalla.fill(ai_configuraciones.bg_color)
    nave.blitme()
    #hacer visible la pantalla dibujanda mas reciente        
    pygame.display.flip()           