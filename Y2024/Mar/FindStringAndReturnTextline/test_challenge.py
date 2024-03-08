import unittest

from Y2024.Mar.FindStringAndReturnTextline.challenge import \
    find_string_and_return_textline


class TestFindStringAndReturnTextline(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_text = """
In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.
In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and
a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem.
Big O notation is also used in many other fields to provide similar estimates.
"""
    def test_notation(self):
        expected_ans = """Line 1: In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.
Line 2: In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and
Line 4: Big O notation is also used in many other fields to provide similar estimates."""
        ans = find_string_and_return_textline(self.sample_text, "notation")
        self.assertEqual(ans, expected_ans)

    def test_fields(self):
        expected_ans = "Line 4: Big O notation is also used in many other fields to provide similar estimates."
        ans = find_string_and_return_textline(self.sample_text, "fields")
        self.assertEqual(ans, expected_ans)

    def test_requirements_similar(self):
        expected_ans = """Line 1: In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.
Line 4: Big O notation is also used in many other fields to provide similar estimates."""
        ans = find_string_and_return_textline(self.sample_text, "requirements, similar")
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

