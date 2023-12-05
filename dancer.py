import pygame
from fsm import FSM

class Dancer(pygame.sprite.Sprite):
    super().__init__()

    self.game = game

    # Load initial image
    self.image = pygame.image.load("assets/images/bot.png")
    self.rect = self.image.get_rect()

    self.fsm = FSM()
    self.init_fsm()
    self.STRONG, self.MILD, self.WEAK, self.OUT = 0, 1, 2, 3
    self.state_transitions = {}   

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
        
    def changeMILK(self):

    def changeSTRONG(self):
