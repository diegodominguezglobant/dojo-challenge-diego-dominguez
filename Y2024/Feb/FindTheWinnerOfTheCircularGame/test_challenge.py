import unittest

from Y2024.Feb.FindTheWinnerOfTheCircularGame.challenge import find_the_winner


class TestLinkedList(unittest.TestCase):
    def test_every_other(self):
        players = [x for x in range(1, 6)]
        k = 2
        winner = find_the_winner(players, k)

        self.assertEqual(winner, 3)

    def test_k_is_n_minus_one(self):
        players = [x for x in range(1, 7)]
        k = 5
        winner = find_the_winner(players, k)

        self.assertEqual(winner, 1)

    def test_k_grater_than_len_of_n(self):
        players = [x for x in range(1, 7)]
        k = 9
        winner = find_the_winner(players, k)

        self.assertEqual(winner, 5)

if __name__ == '__main__':
    unittest.main()
