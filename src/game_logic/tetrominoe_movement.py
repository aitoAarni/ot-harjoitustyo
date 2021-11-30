

class MoveTetrominoe:
    def __init__(self):
        self.left_pressed = False
        self.right_pressed = False


    def activate_movement(self, right=False, left=False):
        self.right_pressed = right
        self.left_pressed = left

    def move_tetrominoe(self):
        self.move_tetrominoe_right = False
        self.move_tetrominoe_left = False
        # Move left
        if self.left_pressed and not self.right_pressed:
            self.move_tetrominoe_left = True

        # Move right
        if self.right_pressed and not self.left_pressed:
            self.move_tetrominoe_right = True

        self.move_tetrominoe_down = True
