## Base imports
import pygame, os, sys

## File imports
from settings import *
from src.scripts.scene_manager import SceneManager

## Main class
class Main:
    def __init__(self):
        ## Core variables & components
        self.KEEP_UP = True
        self.SM = SceneManager(self)
        self.window = pygame.display.set_mode(WINDOW_RES)
    
        ## DEBUG
        self.SM.go_to_scene("title_screen")
        print(self.SM)
        self.SM.go_to_scene("Game")
        print(self.SM)
        self.SM.go_to_scene("Inventory")
        print(self.SM)
        self.SM.leave_scene()
        print(self.SM)
        self.SM.go_to_scene("Shop")
        print(self.SM)
        self.SM.leave_scene()
        print(self.SM)
        self.SM.leave_scene()
        print(self.SM)

    def update(self):
        pass

    def draw(self):
        self.window.fill((30, 30, 30))
        ## Draw calls go here

        ## Draw calls end here
        pygame.display.flip()

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