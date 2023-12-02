import unittest
from event1_part2 import numLetterToDigits, calculateCalibrationValue

class Event1_part2_TestCase(unittest.TestCase):
    def test_replace_1(self):
        """ replace first letters with corresponding digit """
        text = "xtwone3four"
        result = numLetterToDigits(text)
        self.assertEqual(result, "x2wone34our")

    def test_replace_2(self):
        """ replace first letters with corresponding digit """
        text = "two1nine"
        result = numLetterToDigits(text)
        self.assertEqual(result, "2wo19ine")

    def test_replace_3(self):
        """ replace first letters with corresponding digit """
        text = "abcone2threexyz"
        result = numLetterToDigits(text)
        self.assertEqual(result, "abc1ne23hreexyz")

    def test_replace_4(self):
        """ replace first letters with corresponding digit """
        text = "4nineeightseven2"
        result = numLetterToDigits(text)
        self.assertEqual(result, "49ineeight7even2")

    def test_replace_5(self):
        """ replace first letters with corresponding digit """
        text = "zoneight234"
        result = numLetterToDigits(text)
        self.assertEqual(result, "z1n8ight234")

    def test_replace_6(self):
        """ replace first letters with corresponding digit """
        text = "ptwonefive2threekfrtvnbmplpsevenseven"
        result = numLetterToDigits(text)
        self.assertEqual(result, "p2wonefive2threekfrtvnbmplpseven7even")

    def test_replace_7(self):
        """ replace first letters with corresponding digit """
        text = "97dlrqzvfour6594oneightltg"
        result = numLetterToDigits(text)
        self.assertEqual(result, "97dlrqzv4our6594on8ightltg")

    def test_calibrationValue(self):
        """ test calibration value """
        lines = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        for i, line in enumerate(lines):
            lines[i] = numLetterToDigits(line)
        result = calculateCalibrationValue(lines)
        self.assertEqual(result, 281)  # add assertion here


if __name__ == '__main__':
    unittest.main()
