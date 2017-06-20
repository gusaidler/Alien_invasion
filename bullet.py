'''
Created on 19 de jun de 2017

@author: gusta
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship'''
    
    def __init__(self, ai_settings, screen, ship):
        '''Create a bullet object at the ship current position.'''
        super().__init__()
        self.screen = screen
        
        #Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Store the bullet position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    
    def update(self):
        '''Move the bullet up the screen'''
        #Update the decumal position of the bullet.
        #When a bullet is fired, it moves up the screen, which corresponds to a decreasing y-coordinate value
        self.y -= self.speed_factor
        #Update the rect position
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)