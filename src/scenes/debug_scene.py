## Base imports
import pygame, os, sys, math, random, time

## File imports
from src.scripts.scene import Scene
from src.scripts.ui_components import *

## Debug scene!
class DebugScene(Scene):
    def __init__(self, main):
        super().__init__(main)
        self.CLEAR_COLOR = (255, 0, 150)
    
    def update(self):
        print("Hahahahah")
        return super().update()
    
    def draw(self):
        return super().draw()