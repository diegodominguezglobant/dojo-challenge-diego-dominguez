import unittest

from Y2024.Mar.LetterTally.challenge import letter_tally


class TestLetterTally(unittest.TestCase):
    def test_potato(self):
        word = 'potato'
        ans = letter_tally(word)
        expected = {'p': 1, 'a': 1, 'o': 2, 't': 2}
        assert ans == expected

class TestLetterTally(unittest.TestCase):
    def test_pizzzaaa(self):
        word = 'pizzaaaa'
        ans = letter_tally(word)
        expected = {'z': 2, 'a': 4, 'p': 1, 'i': 1}
        assert ans == expected

if __name__ == '__main__':
    unittest.main()

