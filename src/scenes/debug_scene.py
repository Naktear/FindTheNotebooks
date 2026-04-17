## Base imports
import pygame, os, sys, math, random, time

## File imports
from src.scripts.scene import Scene

## Debug scene!
class DebugScene(Scene):
    def __init__(self, main):
        super().__init__(main)