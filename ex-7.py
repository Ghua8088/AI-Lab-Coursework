#Alpha-Beta Pruning for tic-tac-
infinity=float('inf')
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
    print()
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
    
def minimax(board,depth,is_maximizing):
    alpha= -infinity
    beta=  infinity
    winner = check_winner(board)
    if winner is not None:
        if winner == 'X':
            return 10 - depth
        else:
            return depth - 10
    if check_draw(board):
        return 0
    if is_maximizing:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    alpha = max(alpha, minimax(board, depth + 1, False))
                    board[i][j] = ' '
                    if alpha >= beta:
                        break
                    board[i][j] = " "
        return alpha
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    beta = min(beta, minimax(board, depth + 1, True))
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
                    board[i][j] = " "
        return beta

def findBestMove(board):
    best = -infinity
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                moveVal = minimax(board, 0, False)
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
        # Human's Move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue
        board[row][col] = "O"
        print("\nAfter Human's Move:")
        print_board(board)
        if check_winner(board):
            print("\nHuman wins!")
            break
        if check_draw(board):
            print("\nIt's a draw!")
            break
        # AI's Move
        bestMove = findBestMove(board)
        board[bestMove[0]][bestMove[1]] = "X"
        print("\nAfter AI's Move:")
        print_board(board)
        if check_winner(board):
            print("\nAI wins!")
            break
        if check_draw(board):
            print("\nIt's a draw!")
            break