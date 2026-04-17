## Base imports

## Scene class
class Scene:
    def __init__(self, main):
        ## Core components
        self.main = main
        self.CLEAR_COLOR = (30, 30, 30)

        ## Scene elements
        self.ui_elements = []

        ## On scene init
        print("Entered scene!")

    def update(self):
        for ui in self.ui_elements:
            ui.update()

    def draw(self):
        for ui in self.ui_elements:
            ui.draw()