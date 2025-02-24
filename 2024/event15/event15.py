
def move(direction, map_, pos):
    y, x = pos
    n_y, n_x = y+direction[0], x+direction[1]
    if 0 <= n_y < len(map_) and 0 <= n_x < len(map_[n_y]):
        ch = map_[n_y][n_x]
        if ch != '#':
            if ch == '.':
                map_[y][x] = '.'
                map_[n_y][n_x] = '@'
                pos = (n_y, n_x)
            elif ch == 'O':
                next_ch = ch
                next_pos = (n_y, n_x)
                boxes = []
                while next_ch != '#':
                    if next_ch == 'O':
                        boxes.append(next_pos)
                    elif next_ch == '.':
                        for box_pos in boxes:
                            new_box_pos = box_pos[0] + direction[0], box_pos[1] + direction[1]
                            map_[new_box_pos[0]][new_box_pos[1]] = 'O'
                        map_[pos[0]][pos[1]] = '.'
                        pos = pos[0] + direction[0], pos[1] + direction[1]
                        map_[pos[0]][pos[1]] = '@'
                        break
                    next_pos = (next_pos[0]+direction[0], next_pos[1]+direction[1])
                    next_ch = map_[next_pos[0]][next_pos[1]]
    return map_, pos

def moveUp(map_, pos):
    direction = (-1, 0)
    map_, pos = move(direction, map_, pos)
    return map_, pos


def moveRight(map_, pos):
    direction = (0, 1)
    map_, pos = move(direction, map_, pos)
    return map_, pos


def moveDown(map_, pos):
    direction = (1, 0)
    map_, pos = move(direction, map_, pos)
    return map_, pos


def moveLeft(map_, pos):
    direction = (0, -1)
    map_, pos = move(direction, map_, pos)
    return map_, pos


def findRobotPosition(map_: list[list[str]]):
    for i, row in enumerate(map_):
        if '@' in row:
            j = row.index('@')
            return i, j

    return None


def calc_sum_gps(map_):
    total = 0
    for i, row in enumerate(map_):
        for j, ch in enumerate(row):
            if ch == 'O':
                total += (100 * i) + j
    return total

def main():
    with open('data.txt', 'r') as f:
        map_, moves = f.read().strip().split('\n\n')
        map_ = [[cell for cell in row] for row in map_.split('\n')]
        moves = list(moves)
        # print(map_)
        for row in map_:
            print(''.join(row))

        pos = findRobotPosition(map_)
        print(pos)

        for move in moves:
            if move == '^':
                map_, pos = moveUp(map_, pos)
            elif move == '<':
                map_, pos = moveLeft(map_, pos)
            elif move == '>':
                map_, pos = moveRight(map_, pos)
            elif move == 'v':
                map_, pos = moveDown(map_, pos)

        for row in map_:
            print(''.join(row))
        print(pos)

        res = calc_sum_gps(map_)

        print(res)




if __name__ == '__main__':
    main()
