import unittest

from Y2024.Mar.FindTriangleType.challenge import find_triangle_type


class TestFindTriangleType(unittest.TestCase):
    def test_obtuse(self):
        ans = find_triangle_type(80, 84, 116)
        self.assertEqual(ans, "This triangle is a Right triangle")

    def test_right(self):
        ans = find_triangle_type(17, 13, 23)
        self.assertEqual(ans, "This triangle is a Obtuse triangle")

    def test_acute(self):
        ans = find_triangle_type(45, 55, 70)
        self.assertEqual(ans, "This triangle is a Acute triangle")


if __name__ == '__main__':
    unittest.main()

