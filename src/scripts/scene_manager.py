class SceneManager:
    def __init__(self, main):
        ## Core components
        self.main = main
        self.scene_stack = []
        self.current_scene = None
        self.previous_scene = None

    def actualize_the_fucking_scenes(self):
        self.current_scene = self.scene_stack[-1]
        if len(self.scene_stack) > 1:
            self.previous_scene = self.scene_stack[-2]
        else:
            self.previous_scene = None

    def go_to_scene(self, target_scene):
        self.scene_stack.append(target_scene)
        self.actualize_the_fucking_scenes()

    def leave_scene(self):
        if len(self.scene_stack) > 1:
            self.scene_stack.pop()
        self.actualize_the_fucking_scenes()
    
    def __str__(self):
        return f"scene_stack: {self.scene_stack}\ncurrent_scene: {self.current_scene}\nprevious_scene: {self.previous_scene}\n"