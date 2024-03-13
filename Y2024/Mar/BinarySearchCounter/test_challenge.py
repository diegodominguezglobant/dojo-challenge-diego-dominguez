import unittest

from Y2024.Mar.BinarySearchCounter.challenge import binary_search_counter


class TestBinarySearchCounter(unittest.TestCase):
    def test_binary_search_counter(self):
        nums = [10 , 11, 12, 16, 18, 23, 29, 33, 48, 54, 57 ,68, 77, 84, 98]
        targ = 48
        ans = binary_search_counter(nums, targ)
        self.assertEqual(ans, 8)

if __name__ == '__main__':
    unittest.main()

