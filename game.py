import pygame
from options import Options
from dancer import Dancer

class Game:

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    LPINK = (255, 224, 229)  # Light Pink

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Survive Comp Dance")

        # Initialize images and initial pygame screen
        self.init_images()
        self.game_state = "initial"

        # Paths
        self.txt_grid = []
        self.grid = []

        # Sprites
        self.dancer = Dancer()



    def init_images(self):
    # Load and scale images, and initialize their rects
        self.d1_food = pygame.image.load("images/d1_food.png").convert_alpha()
        self.d1_food = pygame.transform.scale(self.d1_food, (300, 200))
        self.d1_food_rect = self.d1_food.get_rect()  # Rect will be positioned in the run method

        self.d2_food = pygame.image.load("images/d2_food.png").convert_alpha()
        self.d2_food = pygame.transform.scale(self.d2_food, (300, 200))
        self.d2_food_rect = self.d2_food.get_rect()

        self.d3_food = pygame.image.load("images/d3_food.png").convert_alpha()
        self.d3_food = pygame.transform.scale(self.d3_food, (300, 200))
        self.d3_food_rect = self.d3_food.get_rect()

        #make the following below similar 

        self.d1_practice = pygame.image.load("images/d1_practice.png")
        self.d1_practice = pygame.transform.scale(self.d1_practice, (350, 200))
        self.d1_practice_rect = self.d1_practice.get_rect()

        self.d2_practice = pygame.image.load("images/d2_practice.png")
        self.d2_practice = pygame.transform.scale(self.d2_practice, (350, 200))
        self.d2_practice_rect = self.d2_practice.get_rect()

        self.d3_practice = pygame.image.load("images/d3_practice.png")
        self.d3_practice = pygame.transform.scale(self.d3_practice, (350, 200))
        self.d3_practice_rect = self.d3_practice.get_rect()

        self.resultWEAK = pygame.image.load("images/resultWEAK.png")
        self.resultREG = pygame.image.load("images/resultREG.png")
        self.resultSTRONG = pygame.image.load("images/resultSTRONG.png")

        self.finalWEAK = pygame.image.load("images/finalWEAK.png")
        self.finalREG = pygame.image.load("images/finalREG.png")
        self.finalSTRONG = pygame.image.load("images/finalSTRONG.png")

        # hard-coded the image in for the demo
        weak_image = pygame.image.load("images/resultWEAK.png").convert_alpha()
        weak_image = pygame.transform.scale(weak_image, (450, 350))
        self.weak_option = Options(self.screen, weak_image.get_rect(), weak_image, 100, 200)


    def run(self):
        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.check_image_click(event.pos)
                        self.dancer.fsm.process(self.dancer.get_healthPoints())

                        #manually changed the state to weak for the demo purpose
                        self.game_state = "weak"

                        # After processing the FSM, update the game state. Not shown for demo as I couldn't get it to work
                        # current_dancer_state = self.dancer.get_state()
                        # if current_dancer_state <0:
                        #     self.game_state = "out"
                        # elif current_dancer_state <= 1:
                        #     self.game_state = "weak"
                        # elif current_dancer_state <= 3:
                        #     self.game_state = "reg"
                        # elif current_dancer_state <= 5:
                        #     self.game_state = "strong"


            # Clear the screen
            self.screen.fill(self.LPINK)

            # Draw based on the current state
            if self.game_state == "initial":
                # Draw initial options
                self.food_option1 = Options(self.screen, self.d1_food_rect, self.d1_food, 50, 300)
                self.food_option1.drawImg()
                self.food_option2 = Options(self.screen, self.d2_food_rect, self.d2_food, 250, 300)
                self.food_option2.drawImg()
                self.food_option3 = Options(self.screen, self.d3_food_rect, self.d3_food, 450, 300)
                self.food_option3.drawImg()

            elif self.game_state == "weak":
                # Prints weak state image, hard coded for demo
                print("CURRENT STATE IS WEAK")
                self.weak_option.drawImg()
                # self.dancer.changeWEAK() is the correct code, but commented out for demo 

            # Other states not shown in demo
            # elif self.game_state == "practices":
            #     # Draw options for different practice choices, same as food options but for the practice options
            #     self.practice_option1 = Options(self.screen, self.d1_practice_rect, self.d1_practice, 50, 300)
            #     self.practice_option1.drawImg()
            #     self.practice_option2 = Options(self.screen, self.d2_practice_rect, self.d2_practice, 50, 300)
            #     self.practice_option2.drawImg()
            #     self.practice_option3 = Options(self.screen, self.d3_practice_rect, self.d3_practice, 50, 300)
            #     self.practice_option3.drawImg()
            # elif self.game_state == "reg":
            #     # Prints regular state image
            #     self.dancer.changeREG()

            # elif self.game_state == "strong":
            #     # Prints strong state image
            #     self.dancer.changeSTRONG()
            
            # elif self.game_state == "out":
            #     # Prints losing state image and ends the game
            #     print("Your health has run out and the game is over.")
            #     self.dancer.changeLOSE()

            
            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
            
    def check_image_click(self, mouse_pos):

        if self.food_option1.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)
            print("Health points: ", self.dancer.healthPoints)
        elif self.food_option2.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(-1)
            print("Health points: ", self.dancer.healthPoints)
        elif self.food_option3.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)

        # elif self.practice_option1.rect.collidepoint(mouse_pos):
        #     self.dancer.change_healthPoints(1)
        #     print("Health points: ", self.dancer.healthPoints)
        # elif self.practice_option2.rect.collidepoint(mouse_pos):
        #     self.dancer.change_healthPoints(-1)
        #     print("Health points: ", self.dancer.healthPoints)
        # elif self.practice_option3.rect.collidepoint(mouse_pos):
        #     self.dancer.change_healthPoints(1)
    

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
