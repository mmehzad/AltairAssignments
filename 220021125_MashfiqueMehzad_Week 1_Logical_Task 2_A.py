from collections import deque

def edge_to_neighbours(edges):
    neighbours = {}
    for edge in edges:
        if neighbours.get(edge[0]):
            neighbours.get(edge[0]).append(edge[1])
        else:
            neighbours[edge[0]] = [edge[1]]
        
        if neighbours.get(edge[1]):
            neighbours.get(edge[1]).append(edge[0])
        else:
            neighbours[edge[1]] = [edge[0]]

    return neighbours

def BFS(root_node, neighbours):
    queue = deque(root_node)
    marked = {}
    visited = []
    while len(queue):
        # print(queue)
        node = queue.popleft()

        if not marked.get(node):
            visited.append(node)
            marked[node] = True

            for neighbour in neighbours[node]:
                # print(neighbour)
                if not marked.get(neighbour):
                    queue.append(neighbour)

    return visited

if __name__ == '__main__':
    edges_1 = [['a', 'b'], ['b', 'c'], ['d', 'c'], ['d', 'e'], ['f', 'c'], ['g', 'e'], ['a', 'd'], ['h', 'g'], ['i', 'h']]
    edges_2 = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a']]
    edges_3 = [['a', 'b'], ['a', 'c'], ['d', 'f'], ['f', 'e'], ['e', 'd']]

    neighbours_1 = edge_to_neighbours(edges_1)
    neighbours_2 = edge_to_neighbours(edges_2)
    neighbours_3 = edge_to_neighbours(edges_3)

    print(
        len(BFS('a', neighbours_1)) == len(neighbours_1),
        len(BFS('a', neighbours_2)) == len(neighbours_2),
        len(BFS('a', neighbours_3)) == len(neighbours_3)
    )