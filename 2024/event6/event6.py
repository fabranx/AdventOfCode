# https://adventofcode.com/2024/day/6


def find_guard(map_: list[list[str]]) -> tuple[str, tuple[int, int]] | tuple[None, None]:
    for row, line in enumerate(map_):
        for dir_ in ['^', '>', 'v', '<']:
            if dir_ in line:
                col = line.index(dir_)
                return dir_, (row, col)

    return None, None


def go_up(map_: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    new_pos = pos
    for i in reversed(range(row + 1)):
        # print(f"^ {map_[i][col]},{i},{col}")
        if map_[i][col] == '#':
            return False, map_, new_pos
        elif map_[i][col] == '.' or map_[i][col] == '^':
            map_[i][col] = 'X'
            new_pos = (i, col)
        elif map_[i][col] == 'X':
            new_pos = (i, col)

    return True, map_, new_pos


def go_right(map_: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    new_pos = pos
    for j in range(col, len(map_[row])):
        # print(f"> {map_[row][j]}, {row}, {j}")
        if map_[row][j] == '#':
            return False, map_, new_pos
        elif map_[row][j] == '.':
            map_[row][j] = 'X'
            new_pos = (row, j)
        elif map_[row][j] == 'X':
            new_pos = (row, j)

    return True, map_, new_pos


def go_down(map_: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    new_pos = pos
    for i in range(row, len(map_)):
        # print(f"v {map_[i][col]},{i},{col}")
        if map_[i][col] == '#':
            return False, map_, new_pos
        elif map_[i][col] == '.':
            map_[i][col] = 'X'
            new_pos = (i, col)
        elif map_[i][col] == 'X':
            new_pos = (i, col)

    return True, map_, new_pos


def go_left(map_: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    new_pos = pos
    for j in reversed(range(col)):
        # print(f"< {map_[row][j]}, {row}, {j}")
        if map_[row][j] == '#':
            return False, map_, new_pos
        elif map_[row][j] == '.':
            map_[row][j] = 'X'
            new_pos = (row, j)
        elif map_[row][j] == 'X':
            new_pos = (row, j)

    return True, map_, new_pos


def printMap(map_):
    for line in map_:
        print(line)


def main():
    with open('./data.txt', 'r') as f:
        map_ = [[char for char in line.strip()] for line in f.readlines()]

        direction, pos = find_guard(map_)
        # print(f"^ position {pos}")

        isLeave = False
        while not isLeave:
            if direction == '^':
                isLeave, map_, pos = go_up(map_, pos)
                # print(isLeave, pos)
                # printMap(map_)
                if not isLeave:
                    direction = '>'
                else:
                    break

            elif direction == '>':
                isLeave, map_, pos = go_right(map_, pos)
                # print(isLeave, pos)
                # printMap(map_)
                if not isLeave:
                    direction = 'v'
                else:
                    break

            elif direction == 'v':
                isLeave, map_, pos = go_down(map_, pos)
                # print(isLeave, pos)
                # printMap(map_)
                if not isLeave:
                    direction = '<'
                else:
                    break

            elif direction == '<':
                isLeave, map_, pos = go_left(map_, pos)
                # print(isLeave, pos)
                # printMap(map_)
                if not isLeave:
                    direction = '^'
                else:
                    break

        count_x = 0
        for row in map_:
            for char in row:
                if char == 'X':
                    count_x += 1

        # PART ONE
        print(count_x)


if __name__ == '__main__':
    main()
