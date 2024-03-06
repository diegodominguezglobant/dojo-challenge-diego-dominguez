import unittest

from Y2024.Mar.SwappingPairs.challenge import swapping_pairs


class TestSwappingPairs(unittest.TestCase):
    def test_even_length_list(self):
        numbers = [2,7,8,3,1,4]
        ans = swapping_pairs(numbers)
        expected = [7,2,3,8,4,1]
        self.assertEqual(ans, expected)

    def test_odd_length_list(self):
        numbers = [3,6,8,1,5]
        ans = swapping_pairs(numbers)
        expected = [6, 3, 1, 8, 5]
        self.assertEqual(ans, expected)

if __name__ == '__main__':
    unittest.main()

