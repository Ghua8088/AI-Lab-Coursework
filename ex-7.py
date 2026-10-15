#minimax
infinity=float("inf")
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
    print()
def checkwin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None
def checkdraw(board):
    for i in board:
        for j in i:
            if j==" ":
                return False
    return True
def minimax(board,ismaximizing,alpha=-infinity,beta=infinity):
    result=checkwin(board)
    if result=="X":
        return 10
    elif result=="O":
        return -10
    if checkdraw(board):
        return 0
    pruned=False
    if ismaximizing:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== " ":
                    board[i][j]="X"
                    max_eval= max(alpha,minimax(board,False,alpha,beta))
                    alpha=max(alpha,max_eval)
                    board[i][j]=" "
                    if alpha>=beta:
                        pruned=True
                        break
            if pruned:
                break
        return max_eval
    else:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==" ":
                    board[i][j]="O"
                    min_eval= min(beta,minimax(board,True,alpha,beta))
                    beta=min(beta,min_eval)
                    board[i][j]=" "
                    if alpha>=beta:
                        pruned=True
                        break
            if pruned:
                break
        return min_eval
def findBestMove(board):
    best = -infinity
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                moveVal = minimax(board,False)
                board[i][j] = " "
                if moveVal > best:
                    best = moveVal
                    bestMove = (i, j)
    return bestMove
if __name__ == "__main__":
    board = [[" "] * 3 for _ in range(3)]
    print("Initial Board:")
    print_board(board)
    print("\nAI (X) vs Human (O)\n")
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue
        board[row][col] = "O"
        print("\nAfter Human's Move:")
        print_board(board)
        if checkwin(board):
            print("\nHuman wins!")
            break
        if checkdraw(board):
            print("\nIt's a draw!")
            break
        bestMove = findBestMove(board)
        board[bestMove[0]][bestMove[1]] = "X"
        print("\nAfter AI's Move:")
        print_board(board)
        if checkwin(board):
            print("\nAI wins!")
            break
        if checkdraw(board):
            print("\nIt's a draw!")
            break

        
    
