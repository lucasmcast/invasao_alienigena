import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Invasão Alienigina")
	
	#Cria uma espaçonave
	ship = Ship(ai_settings, screen)
	
	# Cria um grupo no qual serão armazenadas os projéteis
	bullets = Group()
	
	#inicia o laço principal do jogo
	while True:
		
		#observa eventos de teclado e de mouse
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		
		# Redesenha a tela a cada passagem pelo laço
		gf.update_screen(ai_settings, screen, ship, bullets)
		

run_game()
