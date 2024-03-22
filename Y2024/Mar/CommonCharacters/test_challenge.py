import unittest

from Y2024.Mar.CommonCharacters.challenge import common_characters


class TestCommonCharacters(unittest.TestCase):
    def test_common_characters1(self):
        my_list_1 = 'acexivou', 'aegihobu'
        expected_ans = 'aeiou'

        ans = common_characters(my_list_1)

        self.assertEqual(ans, expected_ans)

    def test_common_characters2(self):
        my_list = 'abc', 'abc'
        expected_ans = 'abc'

        ans = common_characters(my_list)

        self.assertEqual(ans, expected_ans)

    def test_common_characters_3a(self):
        my_list = 'abcaa', 'adfaa', 'aghaa'
        expected_ans = 'aaa'

        ans = common_characters(my_list)
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

