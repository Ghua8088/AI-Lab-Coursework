import tkinter as tk
from tkinter import messagebox

# --- Logic Engine ---
board = [""] * 9

def eval_board(b):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b_idx, c in win_patterns:
        if b[a] == b[b_idx] == b[c] and b[a] != "":
            return 10 if b[a] == "X" else -10
    return 0

def get_blank(b):
    return [i for i, cell in enumerate(b) if cell == ""]

def minimax(board,depth,isMaximizingPlayer,alpha=float("-inf"),beta=float("inf")):
    score=eval_board(board)
    if score==10:return score-depth
    if score==-10:return score+depth
    remBlank=get_blank(board)
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

def find_best_move(b):
    best_val = float("-inf")
    best_move = -1
    alpha=float("-inf")
    beta=float("inf")
    for i in get_blank(b):
        b[i] = "X"
        move_val = minimax(b, 0, False,alpha,beta)
        b[i] = ""
        if move_val > best_val:
            best_val = move_val
            best_move = i
            alpha=max(alpha,best_val)
    return best_move

# --- GUI Implementation ---
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI (Unbeatable)")
        self.root.resizable(False, False)
        self.root.configure(bg="#222831")

        self.status_label = tk.Label(
            self.root, 
            text="Your Turn (O)", 
            font=("Arial", 16, "bold"), 
            bg="#222831", 
            fg="#EEEEEE", 
            pady=10
        )
        self.status_label.pack()

        # Grid container
        self.frame = tk.Frame(self.root, bg="#393E46")
        self.frame.pack(padx=15, pady=5)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.frame,
                text="",
                font=("Arial", 28, "bold"),
                width=4,
                height=2,
                bg="#EEEEEE",
                activebackground="#00ADB5",
                relief="flat",
                command=lambda idx=i: self.on_click(idx)
            )
            btn.grid(row=i // 3, column=i % 3, padx=3, pady=3)
            self.buttons.append(btn)

        # Reset button
        self.reset_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 12, "bold"),
            bg="#00ADB5",
            fg="white",
            relief="flat",
            command=self.reset_game
        )
        self.reset_btn.pack(pady=12)

    def on_click(self, index):
        global board
        if board[index] != "" or eval_board(board) != 0:
            return

        # Player (O) Move
        board[index] = "O"
        self.update_button(index, "O", "#FF5722")

        if self.check_game_over():
            return

        # AI (X) Move
        self.status_label.config(text="AI is thinking...")
        self.root.update()

        ai_move = find_best_move(board)
        if ai_move != -1:
            board[ai_move] = "X"
            self.update_button(ai_move, "X", "#00ADB5")

        if not self.check_game_over():
            self.status_label.config(text="Your Turn (O)")

    def update_button(self, index, symbol, color):
        self.buttons[index].config(text=symbol, fg=color, state="disabled", disabledforeground=color)

    def check_game_over(self):
        score = eval_board(board)
        if score == 10:
            self.status_label.config(text="AI (X) Wins!")
            messagebox.showinfo("Game Over", "AI (X) won the game!")
            return True
        elif score == -10:
            self.status_label.config(text="You (O) Won!")
            messagebox.showinfo("Game Over", "Congratulations, you won!")
            return True
        elif len(get_blank(board)) == 0:
            self.status_label.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a tie!")
            return True
        return False

    def reset_game(self):
        global board
        board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#EEEEEE")
        self.status_label.config(text="Your Turn (O)")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()