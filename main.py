## Base imports
import pygame, os, sys

## File imports
from settings import *

## Main class
class Main:
    def __init__(self):
        ## Core variables & components
        self.KEEP_UP = True
        
        self.window = pygame.display.set_mode(WINDOW_RES)
    
    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.KEEP_UP:
            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.KEEP_UP = False
                    sys.exit()

## Run the game
if __name__ == "__main__":
    pygame.init()
    game = Main()
    game.run()