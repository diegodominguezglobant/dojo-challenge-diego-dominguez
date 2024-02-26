import unittest

from Y2024.Feb.SwapNumbers.challenge import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_swap_pairs_even(self):
        ll = LinkedList()
        for i in range(1, 7):
            ll.append(i)
        ll.swap_pairs()
        self.assertEqual(ll.to_list(), [2, 1, 4, 3, 6, 5])

    def test_swap_pairs_odd(self):
        ll = LinkedList()
        for i in range(1, 6):
            ll.append(i)
        ll.swap_pairs()
        self.assertEqual(ll.to_list(), [2, 1, 4, 3, 5])

    def test_empty_list(self):
        ll = LinkedList()
        ll.swap_pairs()
        self.assertEqual(ll.to_list(), [])

if __name__ == '__main__':
    unittest.main()
