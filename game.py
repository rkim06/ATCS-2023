
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

        # Initialize images
        self.init_images()

        # Paths
        self.txt_grid = []
        self.grid = []

        # Sprites
        self.dancer = Dancer()

    def init_images(self):
        # Initialize the images
        self.d1_food = pygame.image.load("images/d1_food.png")
        self.d1_food = pygame.transform.scale(self.d1_food, (300, 200))
        #self.d1_food = self.d1_food.resize((100, 250))
        self.d1_food_rect = self.d1_food.get_rect()
        
        self.d2_food = pygame.image.load("images/d2_food.png")
        self.d2_food = pygame.transform.scale(self.d2_food, (300, 200))
        self.d2_food_rect = self.d2_food.get_rect()
        self.d3_food = pygame.image.load("images/d3_food.png")
        self.d3_food = pygame.transform.scale(self.d3_food, (300, 200))
        self.d3_food_rect = self.d3_food.get_rect()

        self.d1_practice = pygame.image.load("images/d1_practice.png")
        self.d1_practice = pygame.transform.scale(self.d1_practice, (350, 200))
        self.d2_practice = pygame.image.load("images/d2_practice.png")
        self.d2_practice = pygame.transform.scale(self.d2_practice, (350, 200))
        self.d3_practice = pygame.image.load("images/d3_practice.png")
        self.d3_practice = pygame.transform.scale(self.d3_practice, (350, 200))

        self.resultWEAK = pygame.image.load("images/resultWEAK.png")
        self.resultREG = pygame.image.load("images/resultREG.png")
        self.resultSTRONG = pygame.image.load("images/resultSTRONG.png")

        self.finalweak = pygame.image.load("images/finalWEAK.png")
        self.finalREG = pygame.image.load("images/finalREG.png")
        self.finalSTRONG = pygame.image.load("images/finalSTRONG.png")

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

            # Fill the screen with a color
            self.screen.fill(self.LPINK)

            # Draw options
            self.food_option1 = Options(self.screen, self.d1_food_rect, self.d1_food, 50, 300)
            self.food_option1.drawImg()
            self.food_option2 = Options(self.screen, self.d2_food_rect, self.d2_food, 250, 300)
            self.food_option2.drawImg()
            self.food_option3 = Options(self.screen, self.d3_food_rect, self.d3_food, 450, 300)
            self.food_option3.drawImg()

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
    
    def drawResult(self, image):
        self.image = pygame.image.load("images/"+image+".png")
    
    def check_image_click(self, mouse_pos):
        if self.food_option1.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)
            print("Health points: ", self.dancer.healthPoints)
        elif self.food_option2.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(-1)
            print("Health points: ", self.dancer.healthPoints)
        elif self.food_option3.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)

        if self.d1_practice.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)
        elif self.d2_practice.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(-1)
        elif self.d3_practice.rect.collidepoint(mouse_pos):
            self.dancer.change_healthPoints(1)
            

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
