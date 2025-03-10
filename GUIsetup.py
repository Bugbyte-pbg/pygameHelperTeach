import pygame
import os
import sys

class PygameGUI:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    

    def __init__(self, width=800, height=600, title="Pygame Window", bg_color=BLACK, font_size=30):
        """
        Initializes Pygame and sets up the GUI window.
        """
        pygame.init()
        self.images = {}
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.running = True  # Game loop flag
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.clock = pygame.time.Clock()
        self.screen.fill(self.bg_color)
        pygame.display.update()
        print(f"Pygame window initialized: {self.width}x{self.height}")


    def loadImage(self, name, filename, scale=None):
        """
        Loads an image file and scales it if needed.
        Adds image to images Dictionary
        """
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found!")
            return None
        
        image = pygame.image.load(filename)

        if scale:
            image = pygame.transform.scale(image, scale)#Scale is a tuple of width x height in pixels

        self.images[name] = image

    def drawImage(self, imageName, x, y):
        """
        Draws an image on the screen
        Users must call this every frame to update dynamically
        """
        if imageName in self.images:
            self.screen.blit(self.images[imageName], (x, y))
        else:
            print(f"Error: Image '{imageName}' not found in self.images!")
        
    def handleEvents(self, run = True):
        """
        Handles Pygame events and allows the window to close.
        """

        self.running = run
        
        if not self.running:
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def drawText(self, text, x, y, color=WHITE):
        """
        Renders text on the screen
        Users must call this every frame to update dynamically
        """
        
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def updateScreen(self):
        pygame.display.update()

    def createHitBox(self, character, scale = .75):
        """
        Creates a collision rectangle for an object.
        """

        hbW = int(character.w * scale)
        hbH = int(character.h * scale)

        hbX = (character.w - hbW) // 2
        hbY = (character.h - hbH) // 2
        
        return pygame.Rect(character.x, character.y, hbW, hbH)
        
    def startCycle(self):
        """
        Place at start of main game loop.
        """
        self.screen.fill(self.bg_color)
        
    def endCycle(self):
        """
        Place at end of main game loop.
        """
        self.handleEvents()
        self.updateScreen()
        self.clock.tick(60)


