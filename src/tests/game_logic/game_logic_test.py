import unittest
import src.game_logic.tetrominoe

class TestTetrominoe(unittest.TestCase):
    def setUp(self) -> None:
        self.tetrominoe = src.game_logic.tetrominoe.Tetrominoe()
    
    def test_constructor_sets_counter_value_right(self):
        self.assertEqual(self.tetrominoe.counter, 0)
    