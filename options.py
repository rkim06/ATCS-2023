import pygame
import sys

class Options(pygame.sprite.Sprite):
    def __init__(self, game, x=, y=, image):
        super().__init__()

        self.game = game
        self.image = image

    #initizalize the  images (des- desicion, res- result)
foodDes_img = pygame.image.load("images/getFood.png")
practiceDes_img = pygame.image.load("images/getPractice.png")
teachfavRes_img = pygame.image.load("images/teachFav.png")

    def drawImg(self, image):
