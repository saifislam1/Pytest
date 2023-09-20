# test.py

import unittest
from main import add_numbers


class TestMainMethods(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
