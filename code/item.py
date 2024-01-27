import pygame
from settings import *
from random import randint
import math

class ItemPlayer:
	def __init__(self,animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'bomber': pygame.mixer.Sound('../audio/bomb.wav'),
		'blood_bottle': pygame.mixer.Sound('../audio/healing.mp3'),
		'energy': pygame.mixer.Sound('../audio/energy.mp3'),
		'snowball': pygame.mixer.Sound('../audio/snowball.mp3'),
		}

	def blood_bottle(self,player,strength,number,groups):
		if player.blood_bottles >= number:
			self.sounds['blood_bottle'].play()
			player.health += strength
			player.blood_bottles -= 1 
			if player.health >= player.stats['health']:
				player.health = player.stats['health']
			self.animation_player.create_particles('blood_bottle',player.rect.center,groups)

	def magic_bottle(self,player,strength,number,groups):
		if player.magic_bottles >= number:
			self.sounds['bomber'].play()
			player.energy += strength
			player.magic_bottles -= 1 
			if player.energy >= player.stats['energy']:
				player.energy = player.stats['energy']
			self.animation_player.create_particles('magic_bottle',player.rect.center,groups)

	def bomb(self, player, number, groups):
		if player.bomb >= number:
			player.bomb -= 1
			self.sounds['bomber'].play()
			
			for i in range(1, 6):
				angle = (i / 6) * 2 * math.pi  
				radius = TILESIZE
				x = player.rect.centerx + int(radius * math.cos(angle)) + randint(-TILESIZE // 3, TILESIZE // 3)
				y = player.rect.centery + int(radius * math.sin(angle)) + randint(-TILESIZE // 3, TILESIZE // 3)
				self.animation_player.create_particles('bomb', (x, y), groups)


	def nuclear_bomb(self, player, groups):
		if player.utimate_stats == 100:
			self.sounds['bomber'].play()
			
			for i in range(1, 6):
				angle = (i / 6) * 2 * math.pi  
				radius = TILESIZE
				x = player.rect.centerx + int(radius * math.cos(angle)) + randint(-TILESIZE // 3, TILESIZE // 3)
				y = player.rect.centery + int(radius * math.sin(angle)) + randint(-TILESIZE // 3, TILESIZE // 3)
				self.animation_player.create_particles('bomb', (x, y), groups)

	def snowball(self,player,number,groups):
		if player.snowball >= number:
			player.snowball -= 1
			self.sounds['snowball'].play()

			if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
			elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
			elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
			else: direction = pygame.math.Vector2(0,1)

			for i in range(1,6):
				if direction.x: #horizontal
					offset_x = (direction.x * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('snowball',(x,y),groups)
				else: # vertical
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('snowball',(x,y),groups)

