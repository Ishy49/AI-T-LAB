def valid(grid, r, c, val):
    for i in range(9):
        if grid[r][i]==val or grid[i][c]==val: return False
    sr, sc = 3*(r//3), 3*(c//3)
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if grid[i][j]==val: return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for val in range(1,10):
                    if valid(grid,r,c,val):
                        grid[r][c]=val
                        if solve(grid): return True
                        grid[r][c]=0
                return False
    return True

puzzle = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9],
]
solve(puzzle)
for row in puzzle: print(row)
