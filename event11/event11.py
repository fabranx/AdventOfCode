# -- Day 11: Cosmic Expansion ---
#
# You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.
# He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.
# Maybe you can help him with the analysis to speed things up?
# The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:
#
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
#
# The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.
# Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.
# In the above example, three columns and two rows contain no galaxies:
#
#    v  v  v
#  ...#......
#  .......#..
#  #.........
# >..........<
#  ......#...
#  .#........
#  .........#
# >..........<
#  .......#..
#  #...#.....
#    ^  ^  ^
#
# These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:
#
# ....#........
# .........#...
# #............
# .............
# .............
# ........#....
# .#...........
# ............#
# .............
# .............
# .........#...
# #....#.......
#
# Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:
#
# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# ............6
# .............
# .............
# .........7...
# 8....9.......
#
# In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)
# For example, here is one of the shortest paths between galaxies 5 and 9:
#
# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# .##.........6
# ..##.........
# ...##........
# ....##...7...
# 8....9.......
#
# This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:
#     Between galaxy 1 and galaxy 7: 15
#     Between galaxy 3 and galaxy 6: 17
#     Between galaxy 8 and galaxy 9: 5
# In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.
# Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

# -- Part Two ---
#
# The galaxies are much older (and thus much farther apart) than the researcher initially estimated.
# Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.
# (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)
# Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?



from itertools import combinations

def rows_columns_to_expand(space_map: list[list[str]]) -> tuple[list[int], list[int]]:
    """ Returns a tuple with 2 lists:
        one list containing the rows to be expanded
        another list containing the columns to be expanded """
    rows_to_expand = []
    column_to_expand = []

    for i, row in enumerate(space_map):
        if all(ch == '.' for ch in row):
            rows_to_expand.append(i)

    for n in range(len(space_map)):
        column = []
        for j in range(len(space_map[n])):
            column.append(space_map[j][n])

        if all(ch == '.' for ch in column):
            column_to_expand.append(n)

    return rows_to_expand, column_to_expand

def distance(g1: tuple[str, tuple[int, int]], g2: tuple[str, tuple[int, int]],
             row_exp: list[int], col_exp: list[int], expansion_rate: int) -> int:
    """ return the distance between 2 galaxies (after expansion) """
    coord1 = g1[1]
    coord2 = g2[1]
    dist_no_exp = abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])
    n_col_exp = 0
    n_row_exp = 0
    for col in col_exp:
        if coord1[1] <= col <= coord2[1] or coord1[1] >= col >= coord2[1]:
            n_col_exp += expansion_rate
    for row in row_exp:
        if coord1[0] <= row <= coord2[0] or coord1[0] >= row >= coord2[0]:
            n_row_exp += expansion_rate

    dist_with_exp = dist_no_exp + n_col_exp + n_row_exp
    return dist_with_exp


def calc_galaxy_distances(galaxies: list[tuple[str, tuple[int, int]]], row_to_expand: list[int], col_to_expand: list[int]) -> tuple[int, int]:
    """ given a list containing galaxies and their coordinates,
        create pairs of between galaxies and sum the distances between pairs of galaxies. """
    galaxies_pair = list(combinations(galaxies, 2))  # creates pairs between galaxies

    sum_distance_part1 = 0  # counter for part 1
    sum_distance_part2 = 0  # counter for part 2
    for pair in galaxies_pair:
        g1, g2 = pair
        dist_g1_g2_part1 = distance(g1, g2, row_to_expand, col_to_expand, expansion_rate=1)
        dist_g1_g2_part2 = distance(g1, g2, row_to_expand, col_to_expand, expansion_rate=1_000_000-1)
        sum_distance_part1 += dist_g1_g2_part1
        sum_distance_part2 += dist_g1_g2_part2

    return sum_distance_part1, sum_distance_part2


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        space = []
        count_galaxy = 0
        galaxy_positions = []
        for row, line in enumerate(file.readlines()):
            space_row = []
            for column, char in enumerate(line.strip()):
                if char == '#':
                    galaxy_positions.append((f'{count_galaxy+1}', (row, column)))
                    space_row.append(str(count_galaxy+1))
                    count_galaxy += 1
                else:
                    space_row.append(char)
            space.append(space_row)

        exp_row, exp_col = rows_columns_to_expand(space)
        print(calc_galaxy_distances(galaxy_positions, exp_row, exp_col))





