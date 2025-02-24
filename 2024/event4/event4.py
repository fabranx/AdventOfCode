# https://adventofcode.com/2024/day/4


XMAS = 'XMAS'

def findAllX(map: list[str]):
    result = []
    for i, row in enumerate(map):
        for j, ch in enumerate(row):
            if ch == 'X':
                result.append((i, j))
    return result

def findAllA(map: list[str]):
    result = []
    for i, row in enumerate(map):
        for j, ch in enumerate(row):
            if ch == 'A':
                result.append((i, j))
    return result


def searchLeft(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col < len(XMAS)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row][col-i]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0

def searchUp(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if row < len(XMAS)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row-i][col]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0


def searchRight(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col + len(XMAS)-1 > len(map[row])-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row][col+i]
        if subtext == XMAS:
            return 1
    return 0


def searchDown(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if row+len(XMAS)-1 > len(map)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row+i][col]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0

def searchLeftUp(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col < len(XMAS)-1 or row < len(XMAS)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row-i][col-i]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0


def searchRightUp(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col + len(XMAS)-1 > len(map[row])-1 or row < len(XMAS)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row-i][col+i]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0


def searchRightDown(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col + len(XMAS)-1 > len(map[row])-1 or row+len(XMAS)-1 > len(map)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row+i][col+i]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0


def searchLeftDown(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    if col < len(XMAS)-1 or row+len(XMAS)-1 > len(map)-1:
        return 0
    else:
        subtext = ''
        for i in range(len(XMAS)):
            subtext += map[row+i][col-i]
        # print(subtext)
        if subtext == XMAS:
            return 1
    return 0

def oppositeMS(ch: str):
    if ch == 'M':
        return 'S'
    if ch == 'S':
        return 'M'
    return ''

def searchX_MAS(start_pos, map):
    row = start_pos[0]
    col = start_pos[1]
    # left UP
    if col - 1 < 0 or row - 1 < 0:
        return 0
    # right UP
    if col + 1 > len(map[row])-1 or row - 1 < 0:
        return 0
    # right DOWN
    if col + 1 > len(map[row])-1 or row+1 > len(map)-1:
        return 0
    # left DOWN
    if col - 1 < 0 or row + 1 > len(map)-1:
        return 0

    left_up_ch = map[row-1][col-1]
    right_down_ch = map[row+1][col+1]

    right_up_ch = map[row-1][col+1]
    left_down_ch = map[row+1][col-1]

    if left_up_ch == 'M' and right_down_ch == oppositeMS('M') or left_up_ch == 'S' and right_down_ch == oppositeMS('S'):
        if right_up_ch == 'M' and left_down_ch == oppositeMS('M') or right_up_ch == 'S' and left_down_ch == oppositeMS('S'):
            return 1

    return 0




def main():
    with open('data.txt', 'r') as f:
        map = [row.strip() for row in f.readlines()]
        # print(map)

        allX = findAllX(map)
        # print(allX)

        # PART ONE
        xmas_finded = 0
        for pos in allX:
            # print(pos)
            xmas_finded += searchLeft(pos, map)
            xmas_finded += searchUp(pos, map)
            xmas_finded += searchRight(pos, map)
            xmas_finded += searchDown(pos, map)
            xmas_finded += searchLeftUp(pos, map)
            xmas_finded += searchLeftDown(pos, map)
            xmas_finded += searchRightUp(pos, map)
            xmas_finded += searchRightDown(pos, map)
        print(xmas_finded)


        # PART TWO
        allA = findAllA(map)
        x_mas_finded = 0
        for pos in allA:
            # print(pos)
            x_mas_finded += searchX_MAS(pos, map)



        print(x_mas_finded)





if __name__ == '__main__':
    main()