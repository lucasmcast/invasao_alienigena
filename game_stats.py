class GameStats():
    """Armazena dados estatísticos da invasão alienigena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_status()

        self.game_active = False

        #Pontuação maxima jamais devera ser reiniciada
        self.high_score = 0
    
    def reset_status(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1