import unittest

from Y2024.Mar.EvenOccurrence.challenge import even_occurrence


class TestEvenOccurrence(unittest.TestCase):
    def test_even_occurrence(self):
        ans = even_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9])

        expected_ans = 9
        self.assertEqual(ans, expected_ans)

    def test_even_occurrence(self):
        ans = even_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9])

        expected_ans = None
        self.assertEqual(ans, expected_ans)

    def test_even_occurrence(self):
        ans = even_occurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4])

        expected_ans = 4
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

