import math

# Check winner
def check_winner(b):
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x,y,z in win:
        if b[x]==b[y]==b[z]!=" ": return b[x]
    return "Draw" if " " not in b else None

# Minimax with path tracking
def minimax(b, isMax, path):
    res = check_winner(b)
    if res == "X": return -1
    if res == "O": return 1
    if res == "Draw": return 0

    scores = []
    moves = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if isMax else "X"
            s = minimax(b, not isMax, path + [i])
            b[i] = " "
            scores.append(s)
            moves.append(path + [i])

    avg = sum(scores)/len(scores)
    if abs(avg - 0) < 1e-9: avg = 0  # handle floating errors
    if round(avg + 1, 1) == 1:  # average == +1
        print("✅ Path with average = +1 :", moves[0])

    return avg + 1  # +1 average

# Best move for AI
def best_move(b):
    best = -math.inf
    move = None
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(b, False, [i])
            b[i] = " "
            if score > best:
                best = score
                move = i
    print(f"Average(+1) for best path: {best}")
    return move

# Display board
def show(b):
    for i in range(0,9,3): print(b[i:i+3])
    print()

# Main Game
def play():
    b = [" "]*9
    print("You = X | AI = O")
    show(b)
    while True:
        m = int(input("Enter move (0–8): "))
        if b[m] != " ":
            print("Invalid!"); continue
        b[m] = "X"
        show(b)
        if check_winner(b): break
        ai = best_move(b)
        b[ai] = "O"
        print(f"AI plays at {ai}")
        show(b)
        if check_winner(b): break
    print("Winner:", check_winner(b))

play()
