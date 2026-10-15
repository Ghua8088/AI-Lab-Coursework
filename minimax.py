board=[""]*9
def eval(board):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != "":
            return 10 if board[a] == "X" else -10
    return 0
def getBlank(board):
    return [i for i, cell in enumerate(board) if cell == ""]
def minimax(board,depth,isMaximizingPlayer,alpha,beta):
    score=eval(board)
    if score==10:return score-depth
    if score==-10:return score+depth
    remBlank=getBlank(board)
    if len(remBlank)==0:
        return 0
    if isMaximizingPlayer:
        bestVal=float("-inf")
        for i in remBlank:
            board[i]="X"
            bestVal=max(bestVal,minimax(board,depth+1,False,alpha,beta))
            alpha=max(alpha,bestVal)
            board[i]=""
            if beta<=alpha:
                break
        return bestVal
    else:
        bestVal=float("inf")
        for i in remBlank:
            board[i]="O"
            bestVal=min(bestVal,minimax(board,depth+1,True,alpha,beta))
            beta=min(beta,bestVal)
            board[i]=""
            if beta<=alpha:
                break
        return bestVal
def find_best_move(board):
    best_val = float("-inf")
    best_move = -1
    for i in getBlank(board):
        board[i] = "X"
        move_val = minimax(board, 0, False)
        board[i] = ""
        if move_val > best_val:
            best_val = move_val
            best_move = i
    return best_move
def play():
    while True:
        print(board)
        move = int(input("Enter your move: "))
        if board[move] != "":
            print("Invalid move")
            continue
        board[move] = "O"
        best_move = find_best_move(board)
        board[best_move] = "X"
        if eval(board) == 10:
            print("X wins")
            break
        if eval(board) == -10:
            print("O wins")
            break
        if len(getBlank(board)) == 0:
            print("Draw")
            break
play()

