import pygame
from fsm import FSM

class Dancer(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        # Load initial image 
        # ADDED try and except
        try:
            self.image = pygame.image.load("assets/images/bot.png")
        except FileNotFoundError:
            print("Error: The image file for the dancer bot was not found.")
        
        self.fsm = FSM()
        self.init_fsm()
        self.STRONG, self.MILD, self.WEAK, self.OUT = 0, 1, 2, 3
        self.state_transitions = {} 
        self.healthPoints = 0  
        self.monthNum = 1

    def init_fsm(self):
        self.fsm.add_transitions(0, self.WEAK, self.changeOUT, self.OUT)
        #should this be 5 or 6
        self.fsm.add_transitions(6, self.WEAK, self.changeMILD, self.MILD)

        #should this be 5 or 6
        self.fsm.add_transitions(5, self.MILD, self.changeWEAK, self.WEAK)
        self.fsm.add_transitions(10, self.MILD, self.changeSTRONG, self.STRONG)

        self.fsm.add_transitions(9, self.STRONG, self.changeMILD, self.MILD)
        self.fsm.add_transitions(15, self.STRONG, self.staySTRONG, self.STRONG)     

    def get_state(self):
        return self.fsm.current_state
    
    def change_healthPoints(self, value):
        self.healthPoints += value
        return self.healthPoints
    
    def changeOUT(self):
        pygame.quit()

        #quits the game ("you had to quite dance because it was too hard on mental and physical health")
        # and displays image on screen?

    def changeWEAK(self):
        pass
        
    def changeMILD(self):
        pass

    def changeSTRONG(self):
        pass
