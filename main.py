## Base imports
import pygame, os, sys

## File imports
from settings import *
from src.scripts.scene_manager import SceneManager

## Scene imports
from src.scenes.debug_scene import DebugScene

## Main class
class Main:
    def __init__(self):
        ## Core variables & components
        self.KEEP_UP = True
        self.SM = SceneManager(self)
        self.window = pygame.display.set_mode(WINDOW_RES)
    
        ## Init
        debug_scene = DebugScene(self)
        self.SM.go_to_scene(debug_scene)

        ## DEBUG

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