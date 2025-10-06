from collections import deque
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
rows, cols = len(maze), len(maze[0])

def bfs(maze, start, goal):
    queue = deque([([start], start)])  
    visited = set()

    while queue:
        path, (x, y) = queue.popleft()
        if (x, y) == goal:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                queue.append((path+[(nx, ny)], (nx, ny)))
    return None

print("BFS Path:", bfs(maze, start, goal))
