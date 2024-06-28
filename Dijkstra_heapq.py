import os
os.system('cls')

from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(input_graph, start_point, end_point):

    output_graph = defaultdict(list)
    for v1, v2, w in input_graph:
        output_graph[v1].append((v2, w))

    record, visited, min_dst = [(0, start_point, [])], set(), {start_point: 0}

    while record:
        length, v1, path = heappop(record)
        if v1 not in visited:
            visited.add(v1)
            path = path + [v1]
            for v2, w in output_graph.get(v1):
                if v2 in visited:
                    continue
                current = min_dst.get(v2)
                if current is None or length + w < current:
                    min_dst[v2] = length + w
                    heappush(record, (min_dst[v2], v2, path))
        
        if v1 == end_point:
            return f'Distance from {start_point} to {end_point} is {length}: {path}.'

if __name__ == '__main__':
    G = [
        ('A', 'B', 2), ('A', 'C', 5), ('A', 'G', 12),
        ('B', 'C', 2), ('B', 'A', 2), ('B', 'E', 2), ('B', 'F', 3),
        ('C', 'A', 5), ('C', 'B', 2), ('C', 'E', 2),
        ('D', 'F', 14), ('D', 'G', 4), ('D', 'E', 4),
        ('E', 'B', 2), ('E', 'C', 2), ('E', 'D', 4),('E', 'G', 3),
        ('G', 'A', 12), ('G', 'D', 4), ('G', 'E', 3),
        ('F', 'B', 3), ('F', 'D', 14)
    ]
    start = input('Start: ')
    end = input('End: ')
    print(dijkstra(G, start, end))