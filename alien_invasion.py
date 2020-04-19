import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Invasão Alienigina")

	#Cria o botao Play
	play_button = Button(ai_settings, screen, "Play")

	# Cria uma instância para armazenar dados estatisticos do jogo
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#Cria uma espaçonave, um grupe de projéteis e um grupo de alienigenas
	ship = Ship(ai_settings, screen)
	aliens = Group()
	bullets = Group()
	
	# Cria a frota de alienigenas
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#inicia o laço principal do jogo
	while True:
		
		#observa eventos de teclado e de mouse
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:	
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		
		# Redesenha a tela a cada passagem pelo laço
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		

run_game()
