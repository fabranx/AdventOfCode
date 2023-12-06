# --- Day 3: Gear Ratios ---
#
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
#


def findAllNumbers(lines):
    found = []
    WIDTH = len(lines)
    for row in range(WIDTH):
        num = ''
        startnum = None
        for column in range(WIDTH):
            if lines[row][column].isdigit():
                if not startnum:
                    startnum = (row, column)
                num += lines[row][column]
            else:
                if num:
                    found.append((num, startnum))
                num = ''
                startnum = None

            if column == WIDTH - 1:  # last character of the row
                if num:
                    found.append((num, startnum))
    return found


def checkLeft(lines, pos):
    # check left
    leftpos = (pos[0], pos[1] - 1)
    if leftpos[1] >= 0:
        leftchar = lines[leftpos[0]][leftpos[1]]
        if not leftchar.isdigit() and leftchar != '.':
            return True
    return False


def checkRight(lines, pos, num):
    # check right
    rightpos = (pos[0], pos[1] + len(num))
    if rightpos[1] < len(lines):
        rightchar = lines[rightpos[0]][rightpos[1]]
        if not rightchar.isdigit() and rightchar != '.':
            return True
    return False


def checkUp(lines, pos, num):
    # check up
    uppos = (pos[0] - 1, pos[1])
    if uppos[0] >= 0:
        up_substring = lines[uppos[0]][uppos[1]:uppos[1] + len(num)]
        up_contain_spec_char = False
        for char in up_substring:
            if not char.isdigit() and char != '.':
                up_contain_spec_char = True
                break
        if up_contain_spec_char:
            return True
    return False


def checkDown(lines, pos, num):
    # check down
    downpos = (pos[0] + 1, pos[1])
    if downpos[0] < len(lines):
        down_substring = lines[downpos[0]][downpos[1]:downpos[1] + len(num)]
        down_contain_spec_char = False
        for char in down_substring:
            if not char.isdigit() and char != '.':
                down_contain_spec_char = True
                break
        if down_contain_spec_char:
            return True
    return False


def checkRightUpDiagonal(lines, pos, num):
    # check right up diagonal
    r_up_pos = (pos[0] - 1, pos[1] + len(num))
    if r_up_pos[0] >= 0 and r_up_pos[1] < len(lines):
        r_up_char = lines[r_up_pos[0]][r_up_pos[1]]
        if not r_up_char.isdigit() and r_up_char != '.':
            return True
    return False


def checkLeftUpDiagonal(lines, pos):
    # check left up diagonal
    l_up_pos = (pos[0] - 1, pos[1] - 1)
    if l_up_pos[0] >= 0 and l_up_pos[1] >= 0:
        l_up_char = lines[l_up_pos[0]][l_up_pos[1]]
        if not l_up_char.isdigit() and l_up_char != '.':
            return True
    return False


def checkLeftDownDiagonal(lines, pos):
    # check left down diagonal
    l_down_pos = (pos[0] + 1, pos[1] - 1)
    if l_down_pos[0] < len(lines) and l_down_pos[1] >= 0:
        l_down_char = lines[l_down_pos[0]][l_down_pos[1]]
        if not l_down_char.isdigit() and l_down_char != '.':
            return True
    return False


def checkRightDownDiagonal(lines, pos, num):
    # check right down diagonal
    r_down_pos = (pos[0] + 1, pos[1] + len(num))
    if r_down_pos[0] < len(lines) and r_down_pos[1] < len(lines):
        r_down_char = lines[r_down_pos[0]][r_down_pos[1]]
        # print(num, r_down_char)
        if not r_down_char.isdigit() and r_down_char != '.':
            return True
    return False


def checkValidNumbers(lines, found):
    validNumbers = []

    for current_num, pos in found:
        if checkLeft(lines, pos) or checkRight(lines, pos, current_num) \
                or checkUp(lines, pos, current_num) or checkDown(lines, pos, current_num) \
                or checkRightUpDiagonal(lines, pos, current_num) or checkLeftUpDiagonal(lines, pos) \
                or checkLeftDownDiagonal(lines, pos) or checkRightDownDiagonal(lines, pos, current_num):
            validNumbers.append(current_num)
            continue

    return validNumbers


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        read = file.readlines()
        readlines = []
        for line in read:
            readlines.append(line.rstrip('\n'))

    foundNumbers = findAllNumbers(readlines)
    validNumbers = checkValidNumbers(readlines, foundNumbers)
    total = 0
    for num in validNumbers:
        total += int(num)

    print(total)
