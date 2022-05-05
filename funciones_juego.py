from ast import alias
from distutils.command import check
import imp
import sys
from time import sleep
from tkinter.tix import Tree
from zoneinfo import available_timezones
import pygame

from nave import Nave
from bala import Bala
from alien import Alien
def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_configuraciones, pantalla,nave,balas)
    elif event.key == pygame.K_q:
        sys.exit()      

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
                    
                           
def actualizar_pantalla(ai_configuraciones, pantalla, nave, aliens, balas):
    #actualiza las imagens en la pantalla y pasa a la nueva pantalla
    # volver a dibujar la pantalla durante cada psada por el bucle        
    pantalla.fill(ai_configuraciones.bg_color)
    #vuelve a dibujar todas las balas dentras de la nave y los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)

    #hacer visible la pantalla dibujanda mas reciente        
    pygame.display.flip()

def update_balas(ai_configuraciones, pantalla, nave, balas, aliens):
    #actualzia la posicionn de las balas y elimina las antieguas
    # actualiza las posciones de las balas
    balas.update()
    #deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
    check_bala_alien_collisions(ai_configuraciones, pantalla, nave, aliens, balas)
    
def check_bala_alien_collisions(ai_configuraciones, pantalla, nave, aliens, balas):
    """Responde  a las colsiones entre balas y aliens """
    #elimina las balas y los aliens que hayan chocacdo
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    if len(aliens) == 0:
        #destruye las balas existentes y crea una nueva flota
        balas.empty()
        crear_flota(ai_configuraciones, pantalla, nave, aliens)


def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    #crea una nueva bala y la agrega al grupo de balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)

def get_number_aliens_x(ai_configuraciones, alien_width):
    """ determina el numero de alienigenas que cabe en un fila"""
    available_space_x = ai_configuraciones.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_configuraciones, nave_heigth, alien_height):
    #Crear columnas de aliens
    available_space_y = (ai_configuraciones.screen_height - (3 * alien_height) - nave_heigth)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number):
    #crea un alien y lo coloca en linea
    alien = Alien(ai_configuraciones, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def crear_flota(ai_configuraciones, pantalla, nave, aliens):
    """crea flota completa"""
    #crea un alien y encuentra el numero de aliens seguidos
    #El espacio entre cada alien es igual a un ancho del alien
    alien = Alien(ai_configuraciones, pantalla)

    number_aliens_x = get_number_aliens_x(ai_configuraciones, alien.rect.width)
    number_rows = get_number_rows(ai_configuraciones, nave.rect.height, alien.rect.height)

    #Crea flota  de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number)

def check_fleet_edges(ai_configuraciones,  aliens, ):
    """Respnde de forma apropiada si algun alien ha lelgado a un borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_configuraciones, aliens)
            break

def change_fleet_direction(ai_configuraciones, aliens):
    """Desciende toda la flota y cambia la direccion de la flota"""
    for alien in aliens.sprites():
        alien.rect.y += ai_configuraciones.fleet_drop_speed
        ai_configuraciones.fleet_direction *= -1

def nave_golpeada(ai_configuraciones, estadisticas, pantalla, nave, aliens, balas):
    """Responde a una nave siendo golpeada por un alien"""
    if estadisticas.naves_restantes > 0:
        estadisticas.naves_restantes -= 1
        # Vacia la lista de aliens y balas
        aliens.empty()
        balas.empty()

        # Crea una nueba flota y centra la nave
        crear_flota(ai_configuraciones, pantalla, nave, aliens)
        nave.centrar_nave()

        #Pausa
        sleep(0.5)
    else:
        estadisticas.game_active = False    
    
def check_aliens_bottom(ai_configuraciones, estadisticas, pantalla, nave, aliens, balas):
    """Comprueba si algun alien ha llegado al final de la pantalla"""
    pantalla_rect = pantalla.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= pantalla_rect.bottom:
            #trata esto de la misma foma que si la nave fuera golpeada
            nave_golpeada(ai_configuraciones, estadisticas, pantalla,nave, aliens, balas)
            break    

def update_aliens(ai_configuraciones,estadisticas, pantalla, nave, aliens, balas):
    """comprueba si la flota esta al borde y luego Actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(ai_configuraciones, aliens)
    aliens.update()
    #busca colisiones de alien-nave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_golpeada(ai_configuraciones, estadisticas, pantalla, nave, aliens, balas)
    #busca aliens que golpean la parte inferior de la pantalla
    check_aliens_bottom(ai_configuraciones,estadisticas, pantalla, nave, aliens, balas)


    

                                    