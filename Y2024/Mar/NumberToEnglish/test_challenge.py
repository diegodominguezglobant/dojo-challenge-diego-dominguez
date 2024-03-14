import unittest

from Y2024.Mar.NumberToEnglish.challenge import number_to_english


class TestNumberToEnglish(unittest.TestCase):
    def test_number_to_english(self):
        num = 7
        ans = number_to_english(num)
        self.assertEqual(ans, 'seven')

    def test_number_to_english(self):
        num = 575
        ans = number_to_english(num)
        self.assertEqual(ans, 'five hundred seventy-five')

    def test_number_to_english(self):
        num = 78_193_512
        ans = number_to_english(num)
        expected_ans = 'seventy-eight million one hundred ninety-three thousand five hundred twelve'
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

