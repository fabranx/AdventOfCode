def findAntennas(map):
    antennas = {}
    for row, line in enumerate(map):
        for col, ch in enumerate(line):
            if ch != '.':
                if ch in antennas:
                    antennas[ch].append((row, col))
                else:
                    antennas[ch] = [(row, col)]
    return antennas


def calcAntinodesPosition(pos1, pos2, mul=None):
    row1, col1 = pos1
    row2, col2 = pos2
    if mul:
        row_diff = abs(row1-row2) * mul
        col_diff = abs(col1-col2) * mul
    else:
        row_diff = abs(row1-row2)
        col_diff = abs(col1-col2)

    antinode1_row = 0
    antinode1_col = 0

    antinode2_row = 0
    antinode2_col = 0

    if row1 > row2:
        antinode1_row = row1 + row_diff
        antinode2_row = row2 - row_diff
    else:
        antinode2_row = row2 + row_diff
        antinode1_row = row1 - row_diff
    if col1 > col2:
        antinode1_col = col1 + col_diff
        antinode2_col = col2 - col_diff
    else:
        antinode2_col = col2 + col_diff
        antinode1_col = col1 - col_diff

    return (antinode1_row, antinode1_col), (antinode2_row, antinode2_col)



def isValid(pos, maxCol, maxRow):
    if 0 <= pos[0] < maxCol and 0 <= pos[1] < maxRow:
        return True
    else:
        return False

def main():
    with open('data.txt', 'r') as f:
        antenna_map = [[ch for ch in line.strip()] for line in f.readlines()]
        print(antenna_map)

    antennas = findAntennas(antenna_map)
    print(antennas)

    antinodesPositions = set()

    for ch in antennas:
        for i in range(len(antennas[ch]) - 1):
            for j in range(i+1, len(antennas[ch])):
                pos1 = antennas[ch][i]
                pos2 = antennas[ch][j]
                ant1, ant2 = calcAntinodesPosition(pos1, pos2)
                for ant in [ant1, ant2]:
                    if isValid(ant, len(antenna_map[0]), len(antenna_map)):
                        antinodesPositions.add(ant)

    print(len(antinodesPositions))

    MAX_ROW = len(antenna_map)
    MAX_COL = len(antenna_map[0])
    antinodesPositions = set()
    ### PART TWO
    for ch in antennas:
        for i in range(len(antennas[ch]) - 1):
            for j in range(i+1, len(antennas[ch])):
                pos1 = antennas[ch][i]
                pos2 = antennas[ch][j]
                mul = 1
                while True:
                    ant1, ant2 = calcAntinodesPosition(pos1, pos2, mul)
                    if isValid(ant1, MAX_COL, MAX_ROW):
                        antinodesPositions.add(ant1)
                    if isValid(ant2, MAX_COL, MAX_ROW):
                        antinodesPositions.add(ant2)
                    if not isValid(ant1, MAX_COL, MAX_ROW) and not isValid(ant2, MAX_COL, MAX_ROW):
                        break
                    mul += 1

    for ch in antennas.keys():
        for pos in antennas[ch]:
            antinodesPositions.add(pos)



    # for i in range(MAX_ROW):
    #     for j in range(MAX_COL):
    #         isPrinted = False
    #         if (i, j) in antinodesPositions:
    #             print('#', end='')
    #             isPrinted = True
    #         for ch in antennas.keys():
    #             if (i, j) in antennas[ch]:
    #                 print(ch, end='')
    #                 isPrinted = True
    #         if not isPrinted:
    #             print('.', end='')
    #     print('')







    print(len(antinodesPositions))









if __name__ == '__main__':
    main()