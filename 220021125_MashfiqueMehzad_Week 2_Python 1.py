import math

def edge_to_neighbours(edges):
    neighbours = {}
    for edge in edges:
        # edge: 0 -> source node | 1 -> dest node | 2 -> cost
        if neighbours.get(edge[0]):
            neighbours.get(edge[0]).append((edge[1], edge[2]))
        else:
            neighbours[edge[0]] = [(edge[1], edge[2])]
        
        if neighbours.get(edge[1]):
            neighbours.get(edge[1]).append((edge[0], edge[2]))
        else:
            neighbours[edge[1]] = [(edge[0], edge[2])]
    
    return neighbours


def dijkstra(neighbours, root_node):
    dist = {node: math.inf for node in neighbours}
    dist[root_node] = 0
    visited = {node: False for node in neighbours}
    visited[root_node] = True
    prev = {node: None for node in neighbours}

    queue = [(root_node, 0)]

    def pop_min(queue):
        min_val = min(queue, key=lambda x: x[1])
        queue.pop(queue.index(min_val))
        return min_val
    
    while len(queue):
        node = pop_min(queue)
        for neighbour, cost in neighbours[node[0]]:
            if dist[node[0]] + cost < dist[neighbour]:
                dist[neighbour] = dist[node[0]] + cost
                prev[neighbour] = node[0]

            if not visited[neighbour]:
                # print("not visited: True")
                visited[neighbour] = True
                queue.append((neighbour, dist[node[0]] + cost))
    
        # print(f"node: {node}\nneighbours: {neighbours[node[0]]}\nqueue: {queue}\ndist: {dist}\n\n")

    return dist, prev

if __name__ == '__main__':
    node_count, edge_count = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(edge_count)]

    distance, trail = dijkstra(edge_to_neighbours(edges), 1)
    print(distance, trail)

    if list(trail.values()).count(None) > 1:
        print(-1)
    else:
        print("Shortest Path: ", end='')

        current_node = node_count
        while trail[current_node]:
            print(current_node, end=' ')
            current_node = trail[current_node]

        print(current_node)