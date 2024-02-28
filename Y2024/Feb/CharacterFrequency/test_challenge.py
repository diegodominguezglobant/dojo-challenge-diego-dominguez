import unittest

from Y2024.Feb.CharacterFrequency.challenge import character_frequency


class TestLinkedList(unittest.TestCase):
    def test_missisippi(self):
        word = "mississippi"
        count = character_frequency(word)
        expected = [('i', 4), ('s', 4), ('p', 2), ('m', 1)]

        self.assertEqual(count, expected)

    def test_miaaiaaippi(self):
        word = 'miaaiaaippi'
        count = character_frequency(word)
        expected = [('a', 4), ('i', 4), ('p', 2), ('m', 1)]

        self.assertEqual(count, expected)

    def test_mmmaaaiiibbb(self):
        word = 'mmmaaaiiibbb'
        count = character_frequency(word)
        expected = [('a', 3), ('b', 3), ('i', 3), ('m', 3)]

        self.assertEqual(count, expected)



if __name__ == '__main__':
    unittest.main()
