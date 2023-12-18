import pygame
from fsm import FSM
from game import Game

class Dancer(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        try:
            self.image = pygame.image.load("assets/images/bot.png")
        except FileNotFoundError:
            print("Error: The image file for the dancer bot was not found.")
        
        self.STRONG, self.REG, self.WEAK, self.OUT = 0, 1, 2, 3
        self.fsm = FSM(self.REG)
        self.init_fsm()
        self.state_transitions = {} 
        self.healthPoints = 0  
        self.monthNum = 1

    def init_fsm(self):
        self.fsm.add_transition(1, self.WEAK, -1, self.changeLOSE, self.OUT)
        self.fsm.add_transition(1, self.WEAK, 1, self.changeWEAK, self.WEAK)
        
        self.fsm.add_transition(2, self.WEAK, -1, self.changeWEAK, self.WEAK)
        self.fsm.add_transition(2, self.WEAK, 1, self.changeREG, self.REG)

        self.fsm.add_transition(3, self.REG, -1, self.changeWEAK, self.WEAK)
        self.fsm.add_transition(3, self.REG, 1, self.changeREG, self.REG)

        self.fsm.add_transition(4, self.REG, -1, self.changeREG, self.WEAK)
        self.fsm.add_transition(4, self.REG, 1, self.changeSTRONG, self.REG)
             
        self.fsm.add_transition(5, self.STRONG, -1, self.changeREG, self.WEAK)
        self.fsm.add_transition(5, self.STRONG, 1, self.changeSTRONG, self.REG)

        self.fsm.add_transition(6, self.STRONG, -1, self.changeSTRONG, self.WEAK)
        self.fsm.add_transition(6, self.STRONG, 1, self.changeSTRONG, self.REG)

    def get_state(self):
        return self.fsm.current_state
    
    def change_healthPoints(self, value):
        self.healthPoints += value
        return self.healthPoints
    
    def changeWEAK(self):
        Game.drawResult("resultWEAK")
        pass
        
    def changeREG(self):
        Game.drawResult("resultREG")
        pass

    def changeSTRONG(self):
        Game.drawResult("resultSTRONG")
        pass

    def changeLOSE(self):
        Game.drawResult("finalWEAK")
        exit

