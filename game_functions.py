import pygame
import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	"""Responde a eventos de pressionamento de teclas e de mouses"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
				
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Responde a pressionamentos de tecla"""
	print(event.key)
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		
	elif event.key == pygame.K_SPACE:
		# Cria um novo projétil e o adiciona ao grupo de projéteis
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		
def check_keyup_events(event, ship):
	"""Responde a soltura de tecla"""
	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
	
 
def update_screen(ai_settings, screen, ship, bullets):
	"""Atualiza as imagens na tela e alterna para nova tela"""
	#Redesenha  a tela a cada passagem pelo laço
	screen.fill(ai_settings.bg_color)
	# Redesenha todos os projéteis atrás da espaçonave e dos alieníginas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	
	#deixa a tela mais recente visivel
	pygame.display.flip()
