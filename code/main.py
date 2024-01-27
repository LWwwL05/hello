import pygame
import sys
from settings import *
from level import Level
from player import Player


class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        
        self.button_image = pygame.image.load('img/button.png').convert_alpha()
        self.button_rect = self.button_image.get_rect(center=(WIDTH // 2, HEIGTH // 2))

        
        self.font = pygame.font.Font(None, 100)

        
        self.is_playing = False

       
        self.current_screen = 0
        self.screens = [
            {'image': pygame.image.load('img/open.png').convert_alpha(),
             'text': 'Click screen',
             },  
            {'image': pygame.image.load('img/second.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/third.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/four.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/five.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/five.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/victory_screen2.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/end_screen.png').convert_alpha(),
             'text': ''},
        ]
        self.victory_images = [
            {'image': pygame.image.load('img/victory_screen1.jpg').convert_alpha(),
             'text': ''}
    ]
        self.end_images = [
            {'image': pygame.image.load('img/end_screen.png').convert_alpha(),
             'text': ''}
    ]
        self.current_victory_image = 0 
        self.current_end_image = 0 

        
        


    def run(self):
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    elif event.key == pygame.K_b:
                        self.level.store_menu()
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Move to the next screen on click
                    self.current_screen += 1
                    if self.current_screen == len(self.screens) - 2:
                        # Start the game when reaching the last screen
                        self.is_playing = True
                        self.current_screen += 1

                if event.type == pygame.MOUSEBUTTONDOWN and raccoon_count_result == 0:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(WATER_COLOR)
            raccoon_count_result = self.level.check_raccoon_count()

            if raccoon_count_result == 0 and  self.is_playing:
                self.is_playing = False
                self.current_screen -= 1
                victory_image = self.victory_images[self.current_victory_image]['image']
                self.screen.blit(victory_image, (0, 0))

            player_health_zero = self.level.end_screen()

            if player_health_zero == True:
                self.is_playing = False
                
                end_screen = self.end_images[self.current_end_image ]['image']
                self.screen.blit(end_screen, (0, 0))


            

            if self.is_playing:
                self.level.run()
            else:
                background_image = self.screens[self.current_screen]['image']
                background_rect = background_image.get_rect()
                self.screen.blit(background_image, background_rect)

                
                if self.screens[self.current_screen].get('button', False) :
                    self.screen.blit(self.button_image, self.button_rect)

                
                text = self.font.render(self.screens[self.current_screen]['text'], True, (255, 255, 255))
                self.screen.blit(text, (WIDTH // 2 - 200, HEIGTH // 2 + 50))

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()