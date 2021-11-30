import pygame as py
from pygame.locals import *
import game_logic.input_events
import game_logic.tetrominoe_movement
import game_logic.tetrominoe
import ui.game_view
import settings


class GameLoop(settings.Settings):
    def __init__(self):
        py.init()
        settings.Settings.__init__(self)
        self.clock = py.time.Clock()
        self.events = game_logic.input_events.Events()
        self.tetrominoes = game_logic.tetrominoe.Tetrominoe()
        self.tetrominoes_movement = game_logic.tetrominoe_movement.MoveTetrominoe()
        self.game_gui = ui.game_view.Game_interface(
            self.width, self.length, self.colors)

    def loop(self):
        while True:
            self.clock.tick(100)

            # check for input events
            self.events.event_loop()

            # if movement keyes are pressed this will execute them
            self.tetrominoes_movement.move_tetrominoe()

            moved = self.tetrominoes.move_tetrominoe(self.tetrominoes_movement.move_tetrominoe_right,
                                                     self.tetrominoes_movement.move_tetrominoe_left, self.tetrominoes_movement.move_tetrominoe_down)

            if moved:
                self.tetrominoes_movement.reset_movement_after_executed
            else:
                self.tetrominoes_movement.activate_movement(
                    self.events.right_pressed, self.events.left_pressed)

            # will be made to its own class just for testing
            if self.tetrominoes.falling_tetrominoe.y >= 700-self.block_side:
                self.tetrominoes.falling_tetrominoe_landed()
                self.tetrominoes.create_new_tetrominoe()

            # draws tetrominoes
            self.game_gui.draw_window(
                self.tetrominoes.falling_tetrominoe, self.tetrominoes.landed_tetrominoes, self.tetrominoes.block_images)

            self.events.reset_keys_pressed()
