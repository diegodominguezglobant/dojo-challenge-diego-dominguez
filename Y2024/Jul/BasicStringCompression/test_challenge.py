import unittest

from Y2024.Jul.BasicStringCompression.challenge import basic_string_compression


class TestBasicStringCompression(unittest.TestCase):
    def test_basic_string_compression_abc(self):
        string = "abc"
        expected_ans = "abc"

        ans = basic_string_compression(string)

        self.assertEqual(ans, expected_ans)

    def test_basic_string_compression_a2b3c3a1(self):
        string = "aabbbccca"
        expected_ans = "a2b3c3a1"

        ans = basic_string_compression(string)

        self.assertEqual(ans, expected_ans)

    def test_basic_string_compression_a2b1c5a3(self):
        string = "aabcccccaaa"
        expected_ans = "a2b1c5a3"

        ans = basic_string_compression(string)

        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

