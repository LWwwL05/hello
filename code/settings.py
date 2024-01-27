WIDTH    = 1920
HEIGTH   = 1080
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
UTIMATE_BAR_WIDTH = 250

ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18
ITEM_INDEX = 2

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# coin bar
UI_COIN_BG_COLOR ='#FFFC9B'
TEXT_COIN_COLOR = '#3E3232'


# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'
UTIMATE_COLOR = 'green'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#selection item
item_data = {
    'blood_bottle':{'strength':20,'number':0,'cooldown':100,'graphic':'../graphics/bottles/blood_bottle.png'},
    'magic_bottle':{'strength':20,'number':0,'cooldown':100,'graphic':'../graphics/bottles/magic_bottle.png'},
    'bomb':{'strength':100,'number':0,'cooldown':100,'graphic':'../graphics/bottles/bomb.png'},
    'snowball':{'strength':20,'number':0,'cooldown':'100','graphic':'../graphics/bottles/snowball.png'}}


utimate_data = {
    'big_boy':{'strength':10000,'graphic':'../graphics/particles/nuclear_bomb/nuclear_bomb.png'}}


# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100 ,'coin':50,'damage':20,'utimate':30,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'coin':50,'damage':40,'utimate':30,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'coin':50,'damage':8,'utimate':30,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'coin':50,'damage':6,'utimate':30,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
