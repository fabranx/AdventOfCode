DIRECTIONS = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
}

DIRECTIONAL_KEYPAD = {
    # '_': (0,0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

NUMERIC_KEYPAD = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    # '_': (3,0),
    '0': (3, 1),
    'A': (3, 2)
}


class Robot:
    def __init__(self, initial_pos):
        self.pos = initial_pos

    def move_arm(self, direction):
        if direction in DIRECTIONS:
            self.pos = (self.pos[0] + DIRECTIONS[direction][0], self.pos[1] + DIRECTIONS[direction][1])

def sortMoves(moves):
    right_moves = moves.count('>')
    up_moves = moves.count('^')
    down_moves = moves.count('v')
    left_moves = moves.count('<')

    new_moves = []
    for _ in range(left_moves):
        new_moves.append('<')
    for _ in range(down_moves):
        new_moves.append('v')
    for _ in range(up_moves):
        new_moves.append('^')
    for _ in range(right_moves):
        new_moves.append('>')



    return new_moves


def find_numericKeypadRobot_moves(button, robotPos):
    button_pos = NUMERIC_KEYPAD[button]
    diff_pos = (button_pos[0] - robotPos[0], button_pos[1] - robotPos[1])
    moves = []
    if diff_pos[0] < 0:
        for _ in range(abs(diff_pos[0])):
            moves.append('^')
    elif diff_pos[0] > 0:
        for _ in range(abs(diff_pos[0])):
            moves.append('v')
    if diff_pos[1] > 0:
        for _ in range(abs(diff_pos[1])):
            moves.append('>')
    elif diff_pos[1] < 0:
        for _ in range(abs(diff_pos[1])):
            moves.append('<')

    moves = sortMoves(moves)
    isValid = check_numericKeypad_valid_moves(moves, robotPos)

    if not isValid:
        moves = moves[::-1]

    if len(moves) > 0:
        moves.append('A')
    return moves


def find_directionalKeypadRobot_moves(button, robotPos):
    button_pos = DIRECTIONAL_KEYPAD[button]
    diff_pos = (button_pos[0] - robotPos[0], button_pos[1] - robotPos[1])
    moves = []
    if diff_pos[0] < 0:
        for _ in range(abs(diff_pos[0])):
            moves.append('^')
    elif diff_pos[0] > 0:
        for _ in range(abs(diff_pos[0])):
            moves.append('v')
    if diff_pos[1] > 0:
        for _ in range(abs(diff_pos[1])):
            moves.append('>')
    elif diff_pos[1] < 0:
        for _ in range(abs(diff_pos[1])):
            moves.append('<')

    moves = sortMoves(moves)
    isValid = check_directionalKeypad_valid_moves(moves, robotPos)

    if not isValid:
        moves = moves[::-1]
    moves.append('A')
    return moves


def check_numericKeypad_valid_moves(moves, pos):
    curr_pos = pos
    for move in moves:
        direction = DIRECTIONS[move]
        curr_pos = (curr_pos[0]+direction[0], curr_pos[1]+direction[1])
        if curr_pos not in NUMERIC_KEYPAD.values():
            return False

    return True


def check_directionalKeypad_valid_moves(moves, pos):
    curr_pos = pos
    for move in moves:
        direction = DIRECTIONS[move]
        curr_pos = (curr_pos[0]+direction[0], curr_pos[1]+direction[1])
        if curr_pos not in DIRECTIONAL_KEYPAD.values():
            return False

    return True

def main():
    # code = '029A'
    solution = 0
    for code in ['129A', '176A', '985A', '170A', '528A']:
        keypad_robot = Robot(NUMERIC_KEYPAD['A'])
        directional_robot1 = Robot(DIRECTIONAL_KEYPAD['A'])
        directional_robot2 = Robot(DIRECTIONAL_KEYPAD['A'])

        total_moves = []
        for button in code:
            # print(button)
            numericKeypad_moves = find_numericKeypadRobot_moves(button, keypad_robot.pos)
            # print(f"NUM KEYPAD ROBOT MOVES: {numericKeypad_moves}")
            for move in numericKeypad_moves:
                directionalKeypad_moves1 = find_directionalKeypadRobot_moves(move, directional_robot1.pos)
                # print(f"DIR KEYPAD ROBOT 1 MOVES: {directionalKeypad_moves1}")
                for directionalKeyPadMove in directionalKeypad_moves1:
                    directionalKeypad_moves2 = find_directionalKeypadRobot_moves(directionalKeyPadMove, directional_robot2.pos)
                    # print(f"DIR KEYPAD ROBOT 2 MOVES: {directionalKeypad_moves2}")
                    for directionalKeyPadMove2 in directionalKeypad_moves2:
                        directional_robot2.move_arm(directionalKeyPadMove2)
                    # print(directionalKeypad_moves2)
                    total_moves.append(directionalKeypad_moves2)
                    directional_robot1.move_arm(directionalKeyPadMove)

                # total_moves.append(directionalKeypad_moves1)
                keypad_robot.move_arm(move)
            # print(f"{button} pressed")
            # print(f"NUM ROBOT ON {keypad_robot.pos}")
            # print(f"DIR ROBOT 1 ON {directional_robot1.pos}")
            # print(f"DIR ROBOT 2 ON {directional_robot2.pos}")

            # total_moves.append(numericKeypad_moves)

        # print(total_moves)
        # print(len(total_moves))
        tot_len = 0
        for moves in total_moves:
            tot_len += len(moves)
        print(tot_len)
        numeric_code = int(code[:-1])
        solution += (tot_len*numeric_code)

    print(solution)




if __name__ == '__main__':
    main()
