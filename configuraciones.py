class Configuraciones():
    #Sirve para almacenar todas las configuraciones de invasion alienigena

    def __init__(self):
        #inicializa las configuraciones del juegoo

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #configuraciones de la nave
        self.factor_velocidad_nave = 1.5

        #configuraciones de balas
        self.bala_factor_velocidad = 1
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60