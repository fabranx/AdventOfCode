from dijkstar import Graph, find_path, NoPathError


FIRST_BYTES = 1024
MAX_Y = 70
MAX_X = 70

def find_nodes(mem_space):
    nodes = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # DOWN,RIGHT,UP,LEFT
    for y, row in enumerate(mem_space):
        for x, cell in enumerate(row):
            if cell != '#':
                node = (y, x)
                reachable_nodes = []
                for dy, dx in directions:
                    if 0 <= y+dy < len(mem_space) and 0<= x+dx < len(row):
                        n_pos = (y+dy, x+dx)
                        if mem_space[n_pos[0]][n_pos[1]] != '#':
                            reachable_nodes.append(n_pos)
                nodes[node] = reachable_nodes
    return nodes

def main():
    with open('data.txt' , 'r') as f:
        falling_bytes = [row.strip().split(',') for row in f.readlines()]
        for i, pos in enumerate(falling_bytes):
            falling_bytes[i] = (int(pos[0]), int(pos[1]))

        print(falling_bytes)

    mem_space = [['.' for col in range(MAX_X+1)] for row in range(MAX_Y+1)]

    ### PART ONE
    # for i in range(FIRST_BYTES):
    #     x, y = falling_bytes[i]
    #     mem_space[y][x] = '#'
    #
    # for row in mem_space:
    #     print(''.join(row))
    #
    # nodes = find_nodes(mem_space)
    # start = (0, 0)
    # end = (MAX_Y, MAX_X)
    #
    # graph = Graph()
    # for node in nodes.keys():
    #     for reachable_node in nodes[node]:
    #         graph.add_edge(node, reachable_node, 1)
    #
    #
    # path = find_path(graph, start, end)
    # print(path)  # total_cost is solution


    ### PART TWO
    for i in range(FIRST_BYTES):
        x, y = falling_bytes[i]
        mem_space[y][x] = '#'

    for i in range(FIRST_BYTES, len(falling_bytes)):
        print(i)
        x, y = falling_bytes[i]
        # print(f"{x},{y}")
        mem_space[y][x] = '#'

        # for row in mem_space:
        #     print(''.join(row))

        nodes = find_nodes(mem_space)
        start = (0, 0)
        end = (MAX_Y, MAX_X)

        graph = Graph()
        for node in nodes.keys():
            for reachable_node in nodes[node]:
                graph.add_edge(node, reachable_node, 1)

        try:
            path = find_path(graph, start, end)
            # print(path)  # total_cost is solution

        except NoPathError:
            print(f"SOLUTION: {x},{y}")
            break


if __name__ == '__main__':
    main()

