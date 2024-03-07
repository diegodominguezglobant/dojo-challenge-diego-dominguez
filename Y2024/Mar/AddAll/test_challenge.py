import unittest

from Y2024.Mar.AddAll.challenge import add_all


class TestAddAll(unittest.TestCase):
    def test_add_all(self):
        nums = [2,7,8,3,1,4]
        ans = add_all(nums)
        self.assertEqual(ans, 25)

    def test_add_zero(self):
        nums = []
        ans = add_all(nums)
        self.assertEqual(ans, 0)

if __name__ == '__main__':
    unittest.main()

