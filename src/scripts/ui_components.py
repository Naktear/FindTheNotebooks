## Base imports
import pygame

## Base UI component
class UI_ELEMENT:
    def __init__(self, scene, x=0, y=0, z_index=0):
        ## Core components
        self.scene = scene
        self.main = scene.main
        self.x, self.y = x, y
        self.width, self.height = 0, 0
        self.z_index = z_index
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        ## Add UI to the scene's UIs
        self.scene.ui_elements.append(self)

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.main.window.blit(self.image, self.rect.topleft)

## Picture class
class Picture(UI_ELEMENT):
    def __init__(self, scene, image=None, x=0, y=0):
        super().__init__(scene, x, y)
        self.image = pygame.Surface((16, 16))
        self.image.fill((67, 158, 255))