'''
Created on 19 de jun de 2017

@author: gusta
'''
import sys
import pygame
from settings import Settings
from ship import Ship

'''
To access the events detected by Pygame, well use the pygame.event.get()
'''

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    
    #Load settings
    ai_settings = Settings()
    
    #create a display window called screen, on which well draw all of the game graphical elements
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    #Make a ship
    ship = Ship(screen)
                
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
             
        # Redraw the screen during each pass through the loop.
        
        screen.fill(ai_settings.bg_color)   
        ship.blitme()
                
        # Make the most recently drawn screen visible.
        pygame.display.flip()
     
run_game()