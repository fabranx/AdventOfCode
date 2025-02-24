
def make_connections(connections):
    connections_map = {}
    for connection in connections:
        pc1, pc2 = connection
        if pc1 not in connections_map:
            connections_map[pc1] = []
        if pc2 not in connections_map:
            connections_map[pc2] = []

        connections_map[pc1].append(pc2)
        connections_map[pc2].append(pc1)
    return connections_map


def find_interconnected_computers(connections_map: dict[str, list]):

    valid_interconnections: set[tuple[str, ...]] = set()
    for key in connections_map.keys():
        # connections = [key]
        for computer in connections_map[key]:
            connections_to_find = [*connections_map[key]]
            connections_to_find.remove(computer)
            for computer_to_find in connections_to_find:
                if computer_to_find in connections_map[computer]:
                    # connections.append(computer)
                    # connections.append(computer_to_find)
                    conn = tuple(sorted([key, computer, computer_to_find]))
                    valid_interconnections.add(conn)


    return valid_interconnections

def starts_with_t(connections: set[tuple[str, ...]]) -> int:
    c = 0
    for connection in connections:
        for computer in connection:
            if computer.startswith('t'):
                c += 1
                break
    return c

def main():
    with open('data.txt', 'r') as f:
        pc_connections = [tuple(connections.strip().split('-')) for connections in f.readlines()]


        print(pc_connections)
        connections_map = make_connections(pc_connections)

        print(connections_map)
        for key, val in connections_map.items():
            print(f"{key}: {val}")

        interconnections = find_interconnected_computers(connections_map)
        print(len(interconnections))
        print(interconnections)

        n = starts_with_t(interconnections)
        print(n)


if __name__ == '__main__':
    main()

