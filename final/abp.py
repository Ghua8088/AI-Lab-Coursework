board=[[" "]*3 for _ in range(3)]
n=len(board)
def eval_winner(board):
    
    for i in range(n):
        if board[i][0]==board[i][1]==board[i][2]!=" ":
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i]!=" ":
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!=" ":
        return board[0][0]
    if board[2][0]==board[1][1]==board[0][2]!=" ":
        return board[1][1] 
def eval_draw(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==" ":
                return False
    return True
def print_board(board):
    print("-"*4*n)
    for i in range(n):
        print("|",end="")
        print(" | ".join(board[i]),end="")
        print("|")
        print("-"*4*n)
def minimax(board,depth,ismaximizing,alpha=-float("inf"),beta=float("inf")):
    status=eval_winner(board)
    if status=="X":
        return 10
    if status=="O":
        return -10
    if eval_draw(board):
        return 0
    if ismaximizing:
        bestval=-float("inf")
        for i in range(n):
            for j in range(n):
                if board[i][j]==" ":
                    board[i][j]="X"
                    bestval=max(bestval,minimax(board,depth+1,not ismaximizing,alpha,beta))
                    board[i][j]=" "
                    alpha=max(bestval,alpha)
                    if beta<=alpha:
                        break
        return bestval
    else:
        bestval=float("inf")
        for i in range(n):
            for j in range(n):
                if board[i][j]==" ":
                    board[i][j]="O"
                    bestval=min(bestval,minimax(board,depth+1,not ismaximizing,alpha,beta))
                    board[i][j]=" "
                    beta=min(bestval,beta)
                    if beta<=alpha:
                        break
        return bestval
def find_bestmove(board):
    bestmove=(-1,-1)
    maxeval=-float("inf")
    for i in range(n):
        for j in range(n):
            if board[i][j]==" ":
                board[i][j]="X"
                val=minimax(board,0,False)
                board[i][j]=" "
                if val>maxeval:
                    bestmove=(i,j)
                    maxeval=val
    return bestmove
def play():
    print("Welcome to TicTacToe:")
    while True:
        rr=int(input("enter the col: "))
        rc=int(input("enter the row: "))
        if board[rr][rc]!=" ":
            print("please enter the coordinates of empty box ")
            continue
        board[rr][rc]="O"
        print_board(board)
        if eval_winner(board)=="O":
            print("You win")
            break
        if eval_draw(board):
            print("draw")
            break
        br,bc=find_bestmove(board)
        board[br][bc]="X"
        print_board(board)
        if eval_winner(board)=="X":
            print("You lose")
            break
        if eval_draw(board):
            print("draw")
            break
play()

    