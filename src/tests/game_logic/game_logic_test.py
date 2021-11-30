import unittest
import src.game_logic.tetrominoes


class TestTetrominoe(unittest.TestCase):
    def setUp(self) -> None:
        self.tetrominoes = src.game_logic.tetrominoes.Tetrominoes()

    def test_constructor_sets_counter_value_right(self):
        self.assertEqual(self.tetrominoes.counter, 0)

    def test_landed_list_empty(self):
        self.assertEqual(self.tetrominoes.landed_tetrominoes, [])

    
    def test_falling_object_generated(self):
        self.assertEqual(len(self.tetrominoes.falling_tetrominoe), 1)
    
