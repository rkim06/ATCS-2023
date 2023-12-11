import pygame
from fsm import FSM

class Dancer(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()

        self.game = game

        # Load initial image
        self.image = pygame.image.load("assets/images/bot.png")
        self.rect = self.image.get_rect()

        self.fsm = FSM()
        self.init_fsm()
        self.STRONG, self.MILD, self.WEAK, self.OUT = 0, 1, 2, 3
        self.state_transitions = {} 
    
        self.healthPoints = 0  
        self.monthNum = 1

        #initizalize the  images 
        d1_food = pygame.image.load("images/d1_food.png")
        d2_food = pygame.image.load("images/d2_food.png")
        d3_food = pygame.image.load("images/d3_food.png")
        d1_practice = pygame.image.load("images/d1_practice.png")
        d2_practice = pygame.image.load("images/d2_practice.png")
        d3_practice = pygame.image.load("images/d3_practice.png")

        decisionTitle_img = pygame.image.load("images/decisionTitle.png")
        teachFav_img = pygame.image.load("images/teachFav.png")

    def init_fsm(self):
        self.fsm.add_transitions(0, self.WEAK, self.changeOUT, self.OUT)
        #should this be 5 or 6
        self.fsm.add_transitions(6, self.WEAK, self.changeMILD, self.MILD)

        #should this be 5 or 6
        self.fsm.add_transitions(5, self.MILD, self.changeWEAK, self.WEAK)
        self.fsm.add_transitions(10, self.MILD, self.changeSTRONG, self.STRONG)

        self.fsm.add_tranistion(9, self.STRONG, self.changeMILD, self.MILD)
        self.fsm.add_transition(15, self.STRONG, self.staySTRONG, self.STRONG)

    def get_state(self):
        return self.fsm.current_state
    
    def changeOUT(self):
        pygame.quit()

        #quits the game ("you had to quite dance because it was too hard on mental and physical health")
        # and displays image on screen?

    def changeWEAK(self):
        pass
        
    def changeMILK(self):
        pass

    def changeSTRONG(self):
        pass
