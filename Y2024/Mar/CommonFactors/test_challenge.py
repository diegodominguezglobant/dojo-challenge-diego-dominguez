import unittest

from Y2024.Mar.CommonFactors.challenge import common_factors


class TestCommonFactors(unittest.TestCase):
    def test_common_factors(self):

        ans = common_factors(10, 20)
        expected_ans = [1, 2, 5]

        self.assertEqual(ans, expected_ans)

    def test_common_factors(self):

        ans = common_factors(7, 9)
        expected_ans = [1]
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

