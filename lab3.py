import heapq
graph = {
    'S': {'A': 2, 'B': 4},
    'A': {'C': 6, 'D': 1},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 3},
    'D': {}
}
heuristic = {
    'S': 7,   # best path is 9, so 7 ≤ 9
    'A': 6,   # from A best cost is 7, so ≤ 7
    'B': 4,   # from B best cost is 5, so ≤ 5
    'C': 1,   # from C best cost is 3, so ≤ 3
    'D': 0    # goal always 0
}

def a_star_search(start, goal):
    pq = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path, g

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")


# Run A* from S → D
path, cost = a_star_search('S', 'D')
print("Optimal Path:", path)
print("Path Cost:", cost)
