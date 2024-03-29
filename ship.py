#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/ADMIN/Documents/pcc-master/chapter_12/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        


# Once the image is loaded, we use get_rect() to access the surface’s rect
# attribute v. One reason Pygame is so efficient is that it lets you treat game 
# elements like rectangles (rects), even if they’re not exactly shaped like rectangles. Treating an element as a rectangle is efficient because rectangles 
# are simple geometric shapes. This approach usually works well enough that 
# no one playing the game will notice that we’re not working with the exact 
# shape of each game element.
# When working with a rect object, you can use the x- and y-coordinates 
# of the top, bottom, left, and right edges of the rectangle, as well as the 
# center. You can set any of these values to determine the current position 
# of the rect.

# In[ ]:




