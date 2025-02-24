from dijkstar import Graph, find_path
# from dijkstar.algorithm import single_source_shortest_paths
import math
import sys


# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def add_edge(self, u, v, weight):
#         if u not in self.graph:
#             self.graph[u] = []
#         self.graph[u].append((v, weight))
#
#     def all_paths_with_costs(self, start, end, path=None, cost=0, all_paths=None):
#         if path is None:
#             path = []
#         if all_paths is None:
#             all_paths = []
#
#         # Aggiungiamo il nodo corrente al percorso
#         path = path + [start]
#
#         # Se raggiungiamo il nodo finale, salviamo il percorso e il costo
#         if start == end:
#             all_paths.append((list(path), cost))
#         else:
#             # Esploriamo i nodi adiacenti
#             for neighbor, weight in self.graph.get(start, []):
#                 if neighbor not in path:  # Evitare cicli
#                     self.all_paths_with_costs(neighbor, end, path, cost + weight, all_paths)
#
#         return all_paths


def find_start_end(maze):
    start = None
    end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i,j)
            if cell == 'E':
                end = (i,j)
        if start and end:
            break
    return start, end


def find_nodes(maze):
    nodes = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # GIU,DESTRA,SU,SINISTRA
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell != '#':
                node = (i, j)
                reachables_edges = []
                for dy, dx in directions:
                    if 0 <= i+dy < len(maze) and 0 <= j+dx < len(row):
                        n_pos = (i+dy, j+dx)
                        if maze[n_pos[0]][n_pos[1]] != '#':
                            reachables_edges.append(n_pos)
                nodes[node] = reachables_edges

    return nodes


def cost_func(u, v, edge, prev_edge):
    if prev_edge is None:
        if edge[1] != (0, 1):
            return 1001
        else:
            return 1
    direction = edge[1]
    prev_direction = prev_edge[1]
    cost = edge[0]
    if direction != prev_direction:
        cost += 1000

    return cost


def main():
    with open('data.txt', 'r') as f:
        maze = [[cell for cell in row.strip()] for row in f.readlines()]
        print(maze)

    start, end = find_start_end(maze)

    edges = find_nodes(maze)

    # print(edges)

    graph = Graph()
    for node in edges.keys():
        for reachable_edge in edges[node]:
            ny, nx = node
            ry, rx = reachable_edge
            d = (ry-ny, rx-nx)
            graph.add_edge(node, reachable_edge, (1, d))



    path = find_path(graph, start, end, cost_func=cost_func)
    print(path)




if __name__ =='__main__':
    main()
