def solve_nqueens(n):
    board = [-1]*n
    solutions = []

    def safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c-col) == abs(r-row):
                return False
        return True

    def backtrack(row):
        if row == n:
            sol = [(r, board[r]) for r in range(n)]
            solutions.append(sol)
            return
        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row+1)
                board[row] = -1  # backtrack step

    backtrack(0)
    return solutions


result = solve_nqueens(6)
print(f"Total solutions for n-Queens: {len(result)}")
for sol in result:
    print(sol)
