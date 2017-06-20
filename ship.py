'''
Created on 19 de jun de 2017

@author: gusta
'''

'''
pygame.image_load() - This function returns a surface representing the ship, which we store in self.image.

Once the image is loaded, we use get_rect() to access the surfaces rect
attribute. One reason Pygame is so efficient is that it lets you treat game
elements like rectangles (rects), even if theyre not exactly shaped like rectangles.
Treating an element as a rectangle is efficient because rectangles
are simple geometric shapes. This approach usually works well enough that
no one playing the game will notice that were not working with the exact
shape of each game element.
When working with a rect object, you can use the x- and y-coordinates
of the top, bottom, left, and right edges of the rectangle, as well as the
center. You can set any of these values to determine the current position
of the rect.
When youre centering a game element, work with the center, centerx, or
centery attributes of a rect. When youre working at an edge of the screen,
work with the top, bottom, left, or right attributes. When youre adjusting
the horizontal or vertical placement of the rect, you can just use the x and
y attributes, which are the x- and y-coordinates of its top-left corner. These
attributes spare you from having to do calculations that game developers
formerly had to do manually, and youll find youll use them often.

In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
increase as you go down and to the right. On a 1200 by 800 screen, the origin is at
the top-left corner, and the bottom-right corner has the coordinates (1200, 800).
Well position the ship at the bottom center of the screen. To do so,
first store the screens rect in self.screen_rect w, and then make the value
of self.rect.centerx (the x-coordinate of the ships center) match the centerx
attribute of the screens rect x. Make the value of self.rect.bottom (the
y-coordinate of the ships bottom) equal to the value of the screen rects
bottom attribute. Pygame will use these rect attributes to position the ship
image so its centered horizontally and aligned with the bottom of the
screen.
At y we define the blitme() method, which will draw the image to the
screen at the position specified by self.rect.


'''

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
         
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        
        #Store a decimal value for the ship center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''Update the ship position based on the movement flag.'''
        
        # Update the ship center value, not the rect.
        # Check if the ship has reached left or right edges before moving it
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

  
print()