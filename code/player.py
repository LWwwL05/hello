import pygame 
from settings import *
from support import import_folder
from entity import Entity
from ui import *




class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic,create_item,create_utimate):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(-6,HITBOX_OFFSET['player'])

		# graphics setup
		self.import_player_assets()
		self.status = 'down'

		# movement 
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites

		# weapon
		self.create_attack = create_attack
		self.destroy_attack = destroy_attack
		self.create_utimate = create_utimate
		self.weapon_index = 0
		self.weapon = list(weapon_data.keys())[self.weapon_index]
		self.can_switch_weapon = True
		self.weapon_switch_time = None
		self.switch_duration_cooldown = 200

		#item
		self.create_item = create_item
		self.selectionitem_index = 0
		self.item = list(item_data.keys())[self.selectionitem_index]
		self.can_switch_item = True
		self.item_switch_time = None
		self.bloodbottle_index = 0

		# magic 
		self.create_magic = create_magic
		self.magic_index = 0
		self.magic = list(magic_data.keys())[self.magic_index]
		self.can_switch_magic = True
		self.magic_switch_time = None

		# stats
		self.stats = {'health': 100,'energy':60,'attack': 10,'magic': 4,'speed': 5}
		self.max_stats = {'health': 300, 'energy': 140,'attack': 20, 'magic' : 10, 'speed': 10}
		self.upgrade_cost = {'health': 100, 'energy': 100,'attack': 100, 'magic' : 100, 'speed': 100}

		#utimate
		self.utimate_stats ={'utimate':10}
		self.utimate_max_stats ={'utimate':300}

		self.utimate = self.utimate_stats['utimate']
		self.utimate_max = self.utimate_stats['utimate']

		self.health = self.stats['health'] * 1
		self.energy = self.stats['energy'] * 1
		
		
		self.exp = 5000
		self.coin = 200
		self.speed = self.stats['speed']

		#item_stats
		self.item_stats = {'bomb':3,'blood_bottles':2,'magic_bottles':3,'snowball':5}
		self.max_item_stats = {'bomb':10,'blood_bottles':10,'magic_bottles':10,'snowball':10}
		self.upgrade_item_cost = {'bomb':100,'blood_bottles':100,'magic_bottles':100,'snowball ':100}

		#item exist
		self.blood_bottles = self.item_stats['blood_bottles'] 
		self.magic_bottles = self.item_stats['magic_bottles'] 
		self.bomb = self.item_stats['bomb'] 
		self.snowball = self.item_stats['snowball'] 


		# damage timer
		self.vulnerable = True
		self.hurt_time = None
		self.invulnerability_duration = 500

		# import a sound
		self.weapon_attack_sound = pygame.mixer.Sound('../audio/sword.wav')
		self.weapon_attack_sound.set_volume(0.4)

	def import_player_assets(self):
		character_path = '../graphics/player/'
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			# movement input
			if keys[pygame.K_UP]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN]:
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

			# attack input 
			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()
				self.weapon_attack_sound.play()

			

			# magic input 
			if keys[pygame.K_LCTRL]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(magic_data.keys())[self.magic_index]
				strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
				cost = list(magic_data.values())[self.magic_index]['cost']
				self.create_magic(style,strength,cost)

			if keys[pygame.K_n]: #item_input
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(item_data.keys())[self.selectionitem_index]
				strength = item_data[list(item_data.keys())[self.selectionitem_index]]['strength']
				number = list(item_data.values())[self.selectionitem_index]['number']
				self.create_item(style,strength,number)
				
			if keys[pygame.K_v] : #item_input
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(utimate_data.keys())[self.selectionitem_index]
				strength = utimate_data[list(utimate_data.keys())[self.selectionitem_index]]['strength']
				self.create_utimate(style,strength)


			if keys[pygame.K_q] and self.can_switch_weapon:
				self.can_switch_weapon = False
				self.weapon_switch_time = pygame.time.get_ticks()
				
				if self.weapon_index < len(list(weapon_data.keys())) - 1:
					self.weapon_index += 1
				else:
					self.weapon_index = 0
					
				self.weapon = list(weapon_data.keys())[self.weapon_index]

			if keys[pygame.K_e] and self.can_switch_magic:
				self.can_switch_magic = False
				self.magic_switch_time = pygame.time.get_ticks()
				
				if self.magic_index < len(list(magic_data.keys())) - 1:
					self.magic_index += 1
				else:
					self.magic_index = 0
					
				self.magic = list(magic_data.keys())[self.magic_index]


			if keys[pygame.K_t] and self.can_switch_item: # item switch functiom
				self.can_switch_item = False
				self.item_switch_time = pygame.time.get_ticks()
				
				if self.selectionitem_index < len(list(item_data.keys())) - 1:
					self.selectionitem_index += 1
				else:
					self.selectionitem_index = 0

			if keys[pygame.K_w]:
				self.health = self.stats['health']
				

	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle','_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack','')
	
	def dead_screen_show(self):
		self.is_playing = False
		end_image = self.end_images[self.current_end_image]['image']
		self.screen.blit(end_image, (0, 0))
		pygame.display.flip()

	def utimate_system(self):
		if self.utimate > self.utimate_max:
			self.utimate = self.utimate_max


	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
				self.attacking = False
				self.destroy_attack()

		if not self.can_switch_weapon:
			if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
				self.can_switch_weapon = True

		if not self.can_switch_magic:
			if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
				self.can_switch_magic = True

		if not self.can_switch_item:
			if current_time - self.item_switch_time >= self.switch_duration_cooldown:
				self.can_switch_item = True

		if not self.vulnerable:
			if current_time - self.hurt_time >= self.invulnerability_duration:
				self.vulnerable = True

	def animate(self):
		animation = self.animations[self.status]

		# loop over the frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

		# flicker 
		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

	def get_full_weapon_damage(self):
		base_damage = self.stats['attack']
		weapon_damage = weapon_data[self.weapon]['damage']
		return base_damage + weapon_damage

	def get_full_magic_damage(self):
		base_damage = self.stats['magic']
		spell_damage = magic_data[self.magic]['strength']
		return base_damage + spell_damage

	def get_value_by_index(self,index):
		return list(self.stats.values())[index]

	def get_cost_by_index(self,index):
		return list(self.upgrade_cost.values())[index]
	
	def get_item_value_by_index(self,index):
		return list(self.item_stats.values())[index]
	
	def get_item_cost_by_index(self,index):
		return list(self.upgrade_item_cost.values())[index]

	def energy_recovery(self):
		if self.energy < self.stats['energy']:
			self.energy += 0.01 * self.stats['magic']
		else:
			self.energy = self.stats['energy']
	def player_health_zero(self):
		if self.health <= 0:
			return True

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.utimate_system()
		self.move(self.stats['speed'])
		self.energy_recovery()