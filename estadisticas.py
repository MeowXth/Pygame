class Estadisticas():
    """Seguimiento de las estadisticas de invasion Alienigena"""
    def __init__(self, ai_configuraciones):
        """Inicializa las estadisticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
        #Inicia invasion alienigena en un estado activo
        self.game_active = False
        


    def reset_stats(self):
        """Inicializa estadisticas que puden cambiar durante el juego"""
        self.naves_restantes = self.ai_configuraciones.cantidad_naves
        self.puntaje = 0
            