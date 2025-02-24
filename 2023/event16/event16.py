# --- Day 16: The Floor Will Be Lava ---
#
# With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.
# Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.
# Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).
# The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.
# You note the layout of the contraption (your puzzle input). For example:
#
# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....
#
# The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:
#
#     If the beam encounters empty space (.), it continues in the same direction.
#     If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
#     If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
#     If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
#
# Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.
# In the above example, here is how the beam of light bounces around the contraption:
#
# >|<<<\....
# |v-.\^....
# .v...|->>>
# .v...v^.|.
# .v...v^...
# .v...v^..\
# .v../2\\..
# <->-/vv|..
# .|<<<2-|.\
# .v//.|.v..
#
# Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):
#
# ######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..
#
# Ultimately, in this example, 46 tiles become energized.
#
# The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

#
# --- Part Two ---
#
# As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)
# So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.
# In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:
#
# .|<2<\....
# |v-v\^....
# .v.v.|->>>
# .v.v.v^.|.
# .v.v.v^...
# .v.v.v^..\
# .v.v/2\\..
# <-2-/vv|..
# .|<<<2-|.\
# .v//.|.v..
#
# Using this configuration, 51 tiles are energized:
#
# .#####....
# .#.#.#....
# .#.#.#####
# .#.#.##...
# .#.#.##...
# .#.#.##...
# .#.#####..
# ########..
# .#######..
# .#...#.#..
#
# Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?


class Beam:
    def __init__(self, start_pos=(0, -1), direction="right"):
        self.pos = start_pos
        self.direction = direction

    def nextPos(self):
        newPos = self.pos
        if self.direction == "right":
            newPos = self.pos[0], self.pos[1] + 1
        elif self.direction == "down":
            newPos = self.pos[0]+1, self.pos[1]
        elif self.direction == "left":
            newPos = self.pos[0], self.pos[1] - 1
        elif self.direction == "up":
            newPos = self.pos[0] - 1, self.pos[1]
        self.pos = newPos
        return self.pos

    def __repr__(self):
        return f"{self.pos} - {self.direction}"

def new_direction_mirror(mirror, old_direction):
    new_dir = old_direction
    if old_direction == "right" and mirror == "\\":
        new_dir = "down"
    elif old_direction == "right" and mirror == "/":
        new_dir = "up"
    elif old_direction == "up" and mirror == "\\":
        new_dir = "left"
    elif old_direction == "up" and mirror == "/":
        new_dir = "right"
    elif old_direction == "left" and mirror == "\\":
        new_dir = "up"
    elif old_direction == "left" and mirror == "/":
        new_dir = "down"
    elif old_direction == "down" and mirror == "\\":
        new_dir = "right"
    elif old_direction == "down" and mirror == "/":
        new_dir = "left"

    return new_dir

def new_direction_splitter(splitter, old_direction, old_pos):
    new_dir = old_direction
    new_beam = None
    if (old_direction == "right" or old_direction == "left") and splitter == "|":
        new_dir = "down"
        new_beam = Beam(old_pos, direction="up")
    elif (old_direction == "up" or old_direction == "down") and splitter == "-":
        new_dir = "left"
        new_beam = Beam(old_pos, direction="right")

    return new_dir, new_beam

def run_beams(grid, beams):
    WIDTH = len(grid)
    MIRRORS = "\\/"
    SPLITTERS = "|-"
    EMPTYSPACE = "."

    energized_tiles = []
    visited_pos = []
    count_no_new_tiles = WIDTH*WIDTH
    while len(beams) > 0:
        for beam in beams:
            i, j = beam.nextPos()
            if (i < 0 or i > WIDTH-1) or (j < 0 or j > WIDTH-1):
                beams.remove(beam)
                continue
            if ((i, j), beam.direction) in visited_pos:  # avoiding loops
                beams.remove(beam)
                continue
            else:
                visited_pos.append(((i, j), beam.direction))

            if not (i, j) in energized_tiles:
                energized_tiles.append((i, j))
            else:
                count_no_new_tiles -= 1

            char = grid[i][j]
            if char != EMPTYSPACE:
                if char in MIRRORS:
                    beam.direction = new_direction_mirror(char, beam.direction)
                elif char in SPLITTERS:
                    new_dir, new_beam = new_direction_splitter(char, beam.direction, beam.pos)
                    beam.direction = new_dir
                    if new_beam is not None:
                        beams.append(new_beam)
    return len(energized_tiles)


if __name__ == '__main__':
    with open('inputData.txt', 'r') as file:
        grid = []
        for line in file.readlines():
            grid.append(line.strip())

    # PART ONE
    print(run_beams(grid, beams=[Beam()]))

    # PART TWO
    p2_beams = []
    for i in range(len(grid)):
        p2_beams.append(Beam(start_pos=(-1, i), direction="down"))
        p2_beams.append(Beam(start_pos=(i, -1), direction="right"))
        p2_beams.append(Beam(start_pos=(len(grid), i), direction="up"))
        p2_beams.append(Beam(start_pos=(i, len(grid)), direction="left"))


    max = 0
    for beam in p2_beams:
        val = run_beams(grid, beams=[beam])
        if val > max:
            max = val

    print(max)

