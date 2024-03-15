import unittest

from Y2024.Mar.FindTheShortestPathBetweenTwoNodes.challenge import \
    find_the_shortest_path_between_two_nodes


class TestFindTheShortestPathBetweenTwoNodes(unittest.TestCase):
    def test_find_the_shortest_path_between_two_nodes(self):
        ad_matrix = [[ 0, 2, 6, 0, 0, 0, 0 ],
                    [ 2, 0, 0, 5, 0, 0, 0 ],
                    [ 6, 0, 0, 8, 0, 0, 0 ],
                    [ 0, 5, 8, 0, 10, 15, 0 ],
                    [ 0, 0, 0, 10, 0, 6, 2 ],
                    [ 0, 0, 0, 15, 6, 0, 6 ],
                    [ 0, 0, 0, 0, 2, 6, 0 ]]


        ans = find_the_shortest_path_between_two_nodes(ad_matrix,0 ,6)
        expected_ans = [0, 1, 3, 4, 6]
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

