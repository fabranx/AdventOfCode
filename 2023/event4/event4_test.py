import unittest
from event4_part1 import splitCards, calculatePoints
from event4_part2 import calculatePileOfScratchcards

class Event4TestCase(unittest.TestCase):
    def test_splitNumbers(self):
        lines = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        card_numbers = splitCards(lines)
        self.assertEqual(card_numbers,
            [
                ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
                ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
                ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
                ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
                ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
                ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
            ]
         )

    def test_calculatePoints(self):
        points_nums = [
                ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
                ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
                ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
                ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
                ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
                ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
            ]
        points = calculatePoints(points_nums)
        self.assertEqual(points, 13)

    def test_calculateScratchcards(self):
        points_nums = [
                ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
                ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
                ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
                ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
                ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
                ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
            ]
        totalCards = calculatePileOfScratchcards(points_nums)
        self.assertEqual(totalCards, 30)



if __name__ == '__main__':
    unittest.main()
