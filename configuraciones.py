class Configuraciones():
    #Sirve para almacenar todas las configuraciones de invasion alienigena

    def __init__(self):
        #inicializa las configuraciones del juegoo

        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (230, 230, 230)

        #configuraciones de la nave
        
        self.cantidad_naves = 3

        #configuraciones de balas
        
        self.bala_width = 30
        self.bala_height = 15
        self.bala_color = 60, 60, 60

        self.balas_allowed = 3

        #Configuraciones de alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #que tan rapido se acelera el juego
        self.escala_aceleracion = 1.1

        self.inicializa_configuraciones_dinamicas()
       

    def inicializa_configuraciones_dinamicas(self):
        """inicializa la configuracion que cambia a lo largo del juego """    
        self.factor_velocidad_nave = 1.5
        self.bala_factor_velocidad = 1
        self.alien_speed_factor = 1
        #fleet_direction, cuando es 1 representa a la derecha; si es -1 representa a la izquierda
        self.fleet_direction = 1
        #Puntuacion
        self.puntos_alien = 50

    def aumentar_velocidad(self):
        """"Aumenta la configuracion de velocidad"""
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.alien_speed_factor *=  self.escala_aceleracion