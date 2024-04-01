import unittest

from Y2024.Apr.PlusMinus.challenge import plus_minus


class TestPlusMinus(unittest.TestCase):
    def test_plus_minus(self):

        ans = plus_minus()
        expected_ans = 3
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

