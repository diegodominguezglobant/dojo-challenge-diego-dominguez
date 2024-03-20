import unittest

from Y2024.Mar.DeepEquality.challenge import (deep_equality,
                                              deep_equality_recursive)


class TestDeepEqualityPythonic(unittest.TestCase):
    def test_deep_equality_false(self):
        x = { 'a': 1, 'b': 2 }
        y = { 'a': 1, 'b': 3 }
        ans = deep_equality(x, y)
        expected_ans = False
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_true(self):
        x = { 'a': 1, 'b': 2 }
        y = { 'a': 1, 'b': 2 }
        ans = deep_equality(x, y)
        expected_ans = True
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_more_levels_true(self):
        x = { 'a': 1, 'b': {'y':8} }
        y = { 'a': 1, 'b': {'y':8} }

        ans = deep_equality(x, y)
        expected_ans = True
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_more_levels_false(self):
        x = { 'a': 1, 'b': {'y': 9} }
        y = { 'a': 1, 'b': {'y': 8} }

        ans = deep_equality(x, y)
        expected_ans = False
        self.assertEqual(ans, expected_ans)


class TestDeepEqualityRecursive(unittest.TestCase):
    def test_deep_equality_false(self):
        x = { 'a': 1, 'b': 2 }
        y = { 'a': 1, 'b': 3 }
        ans = deep_equality_recursive(x, y)
        expected_ans = False
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_true(self):
        x = { 'a': 1, 'b': 2 }
        y = { 'a': 1, 'b': 2 }
        ans = deep_equality_recursive(x, y)
        expected_ans = True
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_more_levels_true(self):
        x = { 'a': 1, 'b': {'y':8} }
        y = { 'a': 1, 'b': {'y':8} }

        ans = deep_equality_recursive(x, y)
        expected_ans = True
        self.assertEqual(ans, expected_ans)

    def test_deep_equality_more_levels_false(self):
        x = { 'a': 1, 'b': {'y': 9} }
        y = { 'a': 1, 'b': {'y': 8} }

        ans = deep_equality_recursive(x, y)
        expected_ans = False
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

