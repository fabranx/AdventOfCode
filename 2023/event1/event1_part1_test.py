import unittest
from event1_part1 import calculateCalibrationValue, getFirstNumber, getLastNumber

class Event1_part1_TestCase(unittest.TestCase):
    def test_getFirstNumber(self):
        """ test first number """
        text = "fs5yyx6a4v"
        result = getFirstNumber(text)
        self.assertEqual(result, "5")  # add assertion here

    def test_getLastNumber(self):
        """ test last number """
        text = "fs5yyx6a4v"
        result = getLastNumber(text)
        self.assertEqual(result, "4")  # add assertion here

    def test_calibrationValue(self):
        """ test calibration value """
        lines = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
        result = calculateCalibrationValue(lines)
        self.assertEqual(result, 142)  # add assertion here

    def test_ValueErrorGetFirstNumber(self):
        """ test value error first number """
        text = "fsyyxav"
        with self.assertRaises(ValueError):  # add assertion here
            result = getFirstNumber(text)

    def test_ValueErrorGetLastNumber(self):
        """ test value error last number """
        text = "fsyyxav"
        with self.assertRaises(ValueError):  # add assertion here
            result = getLastNumber(text)

    def test_ValueErrorCalibrationValue(self):
        """ test calibration value """
        lines = [
            "1abc2",
            "pqrstuvwx", # no digits in this string
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
        with self.assertRaises(ValueError):
            result = calculateCalibrationValue(lines)


if __name__ == '__main__':
    unittest.main()
