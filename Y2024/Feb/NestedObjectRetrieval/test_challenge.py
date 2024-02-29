import unittest

from Y2024.Feb.NestedObjectRetrieval.challenge import find_obj


class TestLinkedList(unittest.TestCase):
    def test_very_nested(self):
        rawData = {
            "info1": {
                "infon": {
                    "textIds": "globantId",
                },
                "texts": {
                    "globantId2": "GLOBANT>>",
                    "globantId": "GLOBANT>",
                    "globantId": {
                        "hola": "hola",
                        "hey": {
                            "hello": 3,
                            "hello2":6,
                            "hellowy": {
                                "textId": "globantIddfgsdfgs"
                            }
                        }
                    }
                },
            },
        }

        ans = find_obj(rawData)
        self.assertEqual(ans, "globantIddfgsdfgs")

    def test_right_there(self):
        rawData = {"textId": "globant1"}

        ans = find_obj(rawData)
        self.assertEqual(ans, "globant1")

if __name__ == '__main__':
    unittest.main()
