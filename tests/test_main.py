import unittest
from unittest.mock import patch

from main import river_crossing


class RiverCrossingTest(unittest.TestCase):
    def test_zero_animals(self):
        with patch('main.sample', return_value=[]):
            path, hate_pairs = river_crossing(0, 1, 0)
        expected = ">>> start                            side_1 = set(), side_2 = set()"
        self.assertEqual(path.strip(), expected)
        self.assertEqual(hate_pairs, [])

    def test_small_case_solution(self):
        pairs = [(0, 1)]
        with patch('main.sample', return_value=pairs):
            path, hate_pairs = river_crossing(3, 2, 1)
        self.assertEqual(hate_pairs, pairs)
        self.assertIn('side_1_ = set()', path)
        self.assertIn('side_2_ = {0, 1, 2}', path)
        self.assertTrue(path.startswith('>>> start'))


if __name__ == '__main__':
    unittest.main()
