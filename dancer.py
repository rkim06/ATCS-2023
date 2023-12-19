import pygame
from fsm import FSM
from options import Options

class Dancer(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        try:
            self.image = pygame.image.load("assets/images/bot.png")
        except FileNotFoundError:
            print("Error: The image file for the dancer bot was not found.")
        
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.LPINK = (255, 224, 229)  # Light Pink
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.STRONG, self.REG, self.WEAK, self.OUT = 0, 1, 2, 3
        self.fsm = FSM(self.REG)
        self.init_fsm()
        self.state_transitions = {} 
        self.healthPoints = 3 
        self.monthNum = 1

        self.resultWEAK = pygame.image.load("images/resultWEAK.png")
        self.resultWEAK_rect = self.resultWEAK.get_rect()
        self.resultREG = pygame.image.load("images/resultREG.png")
        self.resultREG_rect = self.resultREG.get_rect()
        self.resultSTRONG = pygame.image.load("images/resultSTRONG.png")
        self.resultSTRONG_rect = self.resultSTRONG.get_rect()

        self.finalWEAK = pygame.image.load("images/finalWEAK.png")
        self.finalWEAK_rect = self.finalWEAK.get_rect()

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
        #returns an int
        return self.fsm.current_state
    
    def change_healthPoints(self, value):
        if value < 0:
            self.fsm.direction = -1
        else:
            self.fsm.direction = 1
        self.healthPoints += value
        return self.healthPoints
    
    def get_healthPoints(self):
        return self.healthPoints

    # These four functions print the corresponding messages when the health/FSM state is changed
    def changeWEAK(self):
        self.weakImage = pygame.image.load("images/resultWEAK.png")
        self.resultWEAK = Options(self.screen, self.resultWEAK_rect, self.weakImage, 300, 550)
        print("Drawing weak image")
        self.resultWEAK.drawImg()
        pass
        
    def changeREG(self):
        self.screen.fill(self.LPINK)
        self.regImage= pygame.image.load("images/resultREG.png")
        self.resultREG = Options(self.screen, self.resultREG_rect, self.regImage, 300, 550)
        self.resultREG.drawImg()
        pass

    def changeSTRONG(self):
        self.screen.fill(self.LPINK)
        self.strongImg= pygame.image.load("images/resultSTRONG.png")
        self.resultSTRONG = Options(self.screen, self.resultSTRONG_rect, self.strongImg, 300, 550)
        self.resultSTRONG.drawImg()
        pass

    # At this point, the game is also exited as the dancer's health has run out
    def changeLOSE(self):
        self.screen.fill(self.LPINK)
        self.w_finalImg = pygame.image.load("images/finalWEAK.png")
        self.finalWEAK = Options(self.screen, self.finalWEAK_rect, self.w_finalImg, 300, 550)
        self.finalWEAK.drawImg()
        pygame.quit()

