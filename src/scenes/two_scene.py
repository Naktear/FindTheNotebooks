## Base imports
import pygame, os, sys, math, random, time

## File imports
from src.scripts.scene import Scene

## Debug scene!
class TwoScene(Scene):
    def __init__(self, main):
        super().__init__(main)
        self.CLEAR_COLOR = (150, 0, 255)
    
    def update(self):
        print("Heheheheh")
        return super().update()
    
    def draw(self):
        return super().draw()