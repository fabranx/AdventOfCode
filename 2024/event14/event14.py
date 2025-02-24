import math

LENX = 101
LENY = 103


def moveRobot(pos, vel):
    posX, posY = pos
    velX, velY = vel

    n_posX = (posX + velX) % LENX
    n_posY = (posY + velY) % LENY

    return n_posX, n_posY


def printMatrix(robots, i):
    matrix = [[' ' for _ in range(LENX)] for _ in range(LENY)]

    for robot in robots:
        pos, vel = robot
        posX, posY = pos
        matrix[posY][posX] = '#'

    for col in range(LENX):
        column = []
        for row in range(LENY):
            column.append(matrix[row][col])
        column = ''.join(column)
        if '#'*30 in column:
            print(i)
            input()

    # for row in matrix:
    #     r = ''.join(row)
    #     if r.count('########') > 0:
    #         print(i)
    #         print(''.join(row))


def main():
    with open('data.txt', 'r') as f:
        robots = []
        for row in f.readlines():
            pos, vel = row.strip().split()
            posX, posY = pos.split('=')[1].split(',')
            velX, velY = vel.split('=')[1].split(',')
            posX = int(posX)
            posY = int(posY)
            velX = int(velX)
            velY = int(velY)
            robot_pos_vel = ((posX, posY), (velX, velY))
            robots.append(robot_pos_vel)

    print(robots)

    for i in range(10000000):
        for c, robot in enumerate(robots):
            pos, vel = robot
            new_pos = moveRobot(pos, vel)
            robots[c] = ((new_pos[0], new_pos[1]), vel)
            # matrix[new_pos[1]][new_pos[0]] = '#'
        # print(i)
        printMatrix(robots, i)
        # print('\n///////////////////////////////////////////////////////////////\n')

    robots_pos = {}
    for robot in robots:
        pos, vel = robot
        posX, posY = pos
        if posX == LENX // 2 or posY == LENY // 2:
            continue
        if pos in robots_pos:
            robots_pos[pos] = robots_pos[pos] + 1
        else:
            robots_pos[pos] = 1

    print(robots_pos)

    quadrants = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
    }
    for pos in robots_pos:
        posX, posY = pos
        if 0 <= posX < LENX // 2 and 0 <= posY < LENY // 2:
            quadrants['1'] = quadrants['1'] + robots_pos[pos]
        elif LENX // 2 < posX < LENX and 0 <= posY < LENY // 2:
            quadrants['2'] = quadrants['2'] + robots_pos[pos]
        elif 0 <= posX < LENX // 2 and LENY // 2 < posY < LENY:
            quadrants['3'] = quadrants['3'] + robots_pos[pos]
        else:
            quadrants['4'] = quadrants['4'] + robots_pos[pos]

    total = math.prod(quadrants.values())
    print(total)


if __name__ == '__main__':
    main()
