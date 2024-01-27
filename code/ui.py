import pygame
from settings import * 

class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
		self.item_index = 3

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)
		self.utimate_bar_rect =pygame.Rect(10,56,UTIMATE_BAR_WIDTH,BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)
		
		# convert item to dictionary
		self.item_graphics = []
		for item in item_data.values():
			item = pygame.image.load(item['graphic']).convert_alpha()
			self.item_graphics.append(item)


		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			magic = pygame.image.load(magic['graphic']).convert_alpha()
			self.magic_graphics.append(magic)

	def item_box(self,left,top):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE) #SETUP a box size
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect) #draw 
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3) #setup a boarder box colour
		index_text = self.font.render(str(3), True, TEXT_COLOR)
		index_rect = index_text.get_rect(topleft=(left, top))
		self.display_surface.blit(index_text, index_rect)
		return bg_rect




	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,exp):
		text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

	def show_coin(self,coin):
		text_surf = self.font.render(str(int(coin)),False,TEXT_COIN_COLOR)
		x = self.display_surface.get_size()[0] - 100 #X position
		y = self.display_surface.get_size()[1] - 20 #y position
		text_rect = text_surf.get_rect(bottomright = (x, y))

		pygame.draw.rect(self.display_surface,UI_COIN_BG_COLOR,text_rect.inflate(40,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(40,20),3)

	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(10,1005,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def magic_overlay(self,magic_index,has_switched):
		bg_rect = self.selection_box(80,1000,has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf,magic_rect)
	
	def item_overlay(self,selectionitem_index,has_switched):
		bg_rect = self.selection_box(1800,10,has_switched) #display item box on screen
		item_surf = self.item_graphics[selectionitem_index]
		item_rect = item_surf.get_rect(center = bg_rect.center) #

		self.display_surface.blit(item_surf,item_rect)

	def display(self,player): # display ui on screen
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)
		self.show_bar(player.utimate,player.utimate_stats['utimate'],self.utimate_bar_rect,UTIMATE_COLOR)
		

		self.show_exp(player.exp)

		self.show_coin(player.coin)

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
		self.magic_overlay(player.magic_index,not player.can_switch_magic)
		self.item_overlay(player.selectionitem_index,not player.can_switch_item)


	
	
	def update(self):
		
		self.item_box()
		'''

		def update_item_index(self):
        # Decrease the item index when 'w' key is pressed
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.item_index -= 1
			self.item_index = max(0, self.item_index)
		'''