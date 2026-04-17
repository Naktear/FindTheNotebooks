## Base imports

## Scene class
class Scene:
    def __init__(self, main):
        ## Core components
        self.main = main
        self.CLEAR_COLOR = (30, 30, 30)

        ## On scene init
        print("Entered scene!")

    def update(self):
        pass

    def draw(self):
        pass