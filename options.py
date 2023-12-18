import pygame
import sys

class Options(pygame.sprite.Sprite):
    def __init__(self, screen, rect, image, x=100, y=300):
        super().__init__()
        self.image = image
        self.screen = screen
        self.rect = rect
        self.rect.topleft = (x, y)  # Update the position of the rectangle

    def drawImg(self):
        self.screen.blit(self.image, self.rect.topleft)

    # def drawImg(self):
    #     self.screen.blit(self.image, (self.x, self.y))
        
    
