import unittest
from collections import Counter

from Y2024.Mar.SplitListByPivot.challenge import split_list_by_pivot


class TestSplitListByPivot(unittest.TestCase):
    def test_split_list_by_pivot(self):
        this_list = [2,7,8,3,1,4]

        ans = split_list_by_pivot(this_list, 4)
        expected_ans = [[2, 3, 1], [7, 8, 4]]

        assert len(ans) == len(expected_ans)

if __name__ == '__main__':
    unittest.main()
