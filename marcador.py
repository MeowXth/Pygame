import pygame

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

    def prep_puntaje(self):
        """Convierte el marcador en una imagen renderizada"""
        puntaje_str = str(self.estadisticas.puntaje)
        self.puntaje_imagen = self.font.render(puntaje_str, True, self.text_color, self.ai_configuraciones.bg_color)

        #muestra el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_imagen.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20

    def muestra_puntaje(self):
        """Dibuja la puntuacion en la pantalla"""
        self.pantalla.blit(self.puntaje_imagen, self.puntaje_rect)
        
