import unittest

from Y2024.Mar.DiagonalDifference.challenge import diagonal_difference


class TestDiagonalDifference(unittest.TestCase):
    def test_diagonal_difference(self):
        mtx = [
            [1, 2, 3],
            [4, 5, 6],
            [9, 8, 9]
        ]

        ans = diagonal_difference(mtx)
        self.assertEqual(ans, 2)

    def test_1x1(self):
        mtx = [
            [1]
        ]

        ans = diagonal_difference(mtx)
        self.assertEqual(ans, 0)

if __name__ == '__main__':
    unittest.main()

