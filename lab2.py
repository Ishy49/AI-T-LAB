from collections import deque

moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

def is_valid(pos, move):
    if move == 'L' and pos % 3 == 0:
        return False
    if move == 'R' and pos % 3 == 2:
        return False
    if move == 'U' and pos < 3:
        return False
    if move == 'D' and pos > 5:
        return False
    return True

def get_neighbors(state):
    neighbors = []
    zero_pos = state.index('0')
    for m, step in moves.items():
        if is_valid(zero_pos, m):
            new_state = list(state)
            swap_pos = zero_pos + step
            new_state[zero_pos], new_state[swap_pos] = new_state[swap_pos], new_state[zero_pos]
            neighbors.append(''.join(new_state))
    return neighbors

def bfs(start, goal):
    visited = set([start])
    queue = deque([(start, [start])])  # keep track of path

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("BFS for 8-Puzzle:")
            for p in path:
                print(p)
            print("Goal reached!")
            return

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("No solution found.")

# Example run
start_state = "412053786"
goal_state  = "123456780"

bfs(start_state, goal_state)

