import math

# Check winner
def check_winner(board):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in win_combos:
        if board[a]==board[b]==board[c]!=" ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# Minimax algorithm with path tracking
def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            score = minimax(board, not is_max)
            board[i] = " "
            scores.append(score)
    avg = sum(scores)/len(scores) if scores else 0
    return avg + 1  # "+1 average" like the photo

# Best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Display board
def show(board):
    for i in range(0,9,3):
        print(board[i:i+3])
    print()

# Main game
def play():
    board = [" "]*9
    print("You = X | AI = O")
    show(board)
    while True:
        move = int(input("Enter position (0–8): "))
        if board[move] != " ":
            print("Invalid move!")
            continue
        board[move] = "X"
        show(board)
        if check_winner(board): break
        ai = best_move(board)
        board[ai] = "O"
        print(f"AI chooses {ai}")
        show(board)
        if check_winner(board): break

    winner = check_winner(board)
    print("Result:", winner)

play()
