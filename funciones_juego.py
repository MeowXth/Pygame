import sys
import pygame

from nave import Nave
from bala import Bala
def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        #crea una nueva bala y la agrega al grupo de balas
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)    

def verificar_eventos_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False



def verificar_eventos(ai_configuraciones, pantalla, nave, balas):
    #responde a las pulsaciones de teclas y los eventos del raton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event,ai_configuraciones, pantalla, nave, balas)

        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
                    
                           
def actualizar_pantalla(ai_configuraciones, pantalla, nave, balas):
    #actualiza las imagens en la pantalla y pasa a la nueva pantalla
    # volver a dibujar la pantalla durante cada psada por el bucle        
    pantalla.fill(ai_configuraciones.bg_color)
    #vuelve a dibujar todas las balas dentras de la nave y los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    #hacer visible la pantalla dibujanda mas reciente        
    pygame.display.flip()           