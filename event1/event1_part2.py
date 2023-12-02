from event1_part1 import calculateCalibrationValue

letters_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def numLetterToDigits(text: str) -> str:
    found_keys = []
    for key in letters_digits.keys():
        index1 = text.find(key)
        index2 = text.rfind(key)
        if index1 >= 0 and index2 >= 0:
            found_keys.append((index1, key))
            if index2 != index1:
                found_keys.append((index2, key))

    if len(found_keys) > 0:
        found_keys = sorted(found_keys, key=lambda t: t[0])  # sorted by index (t[0])
        for tup in [found_keys[0], found_keys[-1]]:  # consider only the first and last number in letter
            text = text[:tup[0]] + letters_digits[tup[1]] + text[tup[0]+1:]  # replace the first letter of letteral number with the number es. seven => 7even

    return text


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        lines[i] = numLetterToDigits(line)

    with open("outputDataTest.txt", "w") as f:
        f.writelines(lines)

    print(calculateCalibrationValue(lines))

