
def findStartingPositions(trail_map):
    positions = []
    for i, row in enumerate(trail_map):
        for j, ch in enumerate(row):
            if ch == 0:
                positions.append((i, j))
    return positions

def checkUp(pos: tuple[int, int], trail_map):
    row = pos[0]
    col = pos[1]
    num = trail_map[row][col]
    if row - 1 < 0:
        return False, None
    if trail_map[row-1][col] == num+1:
        return True, (row-1, col)
    return False, None


def checkRight(pos: tuple[int, int], trail_map):
    row = pos[0]
    col = pos[1]
    num = trail_map[row][col]
    if col + 1 > len(trail_map[row])-1:
        return False, None
    if trail_map[row][col+1] == num+1:
        return True, (row, col + 1)
    return False, None

def checkDown(pos: tuple[int, int], trail_map):
    row = pos[0]
    col = pos[1]
    num = trail_map[row][col]
    if row + 1 > len(trail_map)-1:
        return False, None
    if trail_map[row+1][col] == num+1:
        return True, (row+1, col)
    return False, None

def checkLeft(pos: tuple[int, int], trail_map):
    row = pos[0]
    col = pos[1]
    num = trail_map[row][col]
    if col - 1 < 0:
        return False, None
    if trail_map[row][col-1] == num+1:
        return True, (row, col - 1)
    return False, None



def findPaths(start: tuple[int, int], trail_map: list[list[int]]):
    paths = [[start]]
    for i in range(1, 10):
        new_paths = []
        for path in paths:
            pos = path[-1]
            next_pos = []
            up, pos_up = checkUp(pos, trail_map)
            right, pos_right = checkRight(pos, trail_map)
            down, pos_down = checkDown(pos, trail_map)
            left, pos_left = checkLeft(pos, trail_map)
            if up:
                next_pos.append(pos_up)
            if right:
                next_pos.append(pos_right)
            if down:
                next_pos.append(pos_down)
            if left:
                next_pos.append(pos_left)

            # if len(next_pos) == 1:
            #     path.append((next_pos[0]))
            if len(next_pos) > 0:
                for n in range(len(next_pos)):
                    new_path = [*path, next_pos[n]]
                    new_paths.append(new_path)
                # path.append((next_pos[0]))
            # else:
            #     paths.remove(path)
        paths = new_paths
    return paths

def main():
    with open('data.txt', 'r') as f:
        trail_map = [[*row.strip()] for row in f.readlines()]
        trail_map = [[int(num) for num in row] for row in trail_map]
        # print(trail_map)

    starting_positions = findStartingPositions(trail_map)
    # print(starting_positions)

    count = 0
    # starting_positions = [(0,2)]
    for start in starting_positions:
        res = findPaths(start, trail_map)
        # print(res)
        # st = set()
        # for p in res:
        #     st.add(p[-1])
        # count += len(st)

        print(len(res))
        count += len(res)

    print(count)



if __name__ == '__main__':
    main()

