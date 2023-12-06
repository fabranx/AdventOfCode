import unittest
from event3_part1 import findAllNumbers, checkRightDownDiagonal, checkLeft, checkLeftDownDiagonal, checkLeftUpDiagonal, checkRightUpDiagonal, checkDown, checkUp, checkRight, checkValidNumbers


class MyTestCase(unittest.TestCase):
    def test_findAllNumbers(self):
        lines = [
            ".242......276....234",
            ".............*......",
            "...548....346.......",
            "....................",
            "....683?...24*......",
            "14-....2...578......",
            "=1.....=.....14..#..",
            ".............*......",
            ".18-489.............",
            "....................",
            "3...................",
            "....................",
            ".....@.........#+...",
            ".........354........",
            "....................",
            "....................",
            "....................",
            "....................",
            "....74..=...-..+...4",
            "...#.....7.8...9..=.",
        ]
        nums = findAllNumbers(lines)
        arr = [num[0] for num in nums]
        self.assertEqual(arr, ['242','276','234','548','346','683','24','14','2','578','1','14','18','489','3','354','74','4','7','8','9'])


if __name__ == '__main__':
    unittest.main()
