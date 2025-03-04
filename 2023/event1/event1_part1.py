# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you
# ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say
# the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you
# into a trebuchet ("please hold still, we need to strap you in").
#
# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been
# amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are
# having trouble reading the values on the document.
#
# The newly-improved calibration document consists of lines of text; each line originally contained a specific
# calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining
# the first digit and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all the calibration values?

def getFirstNumber(text: str) -> str:
    for char in text:
        if char.isdecimal():
            return char
    raise ValueError("no digits in input text")

def getLastNumber(text: str) -> str:
    for char in text[::-1]:
        if char.isdecimal():
            return char
    raise ValueError("no digits in input text")


def calculateCalibrationValue(text_lines):
    sumValue = 0
    for line in text_lines:
        firstnum = getFirstNumber(line)
        lastnum = getLastNumber(line)
        value = f"{firstnum}{lastnum}"
        sumValue += int(value)
    return sumValue


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        lines = file.readlines()

    print(calculateCalibrationValue(lines))
