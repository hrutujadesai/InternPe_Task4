import tkinter as tk

ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

class ConnectFour:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.canvas = tk.Canvas(self.root, width=COLS * 80, height=ROWS * 80)
        self.canvas.pack()
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
        self.message = tk.Label(self.root, text="Player 1's turn")
        self.message.pack()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                x1, y1 = col * 80, row * 80
                x2, y2 = x1 + 80, y1 + 80
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                if self.board[row][col] == PLAYER1:
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
                elif self.board[row][col] == PLAYER2:
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="black")

    def check_winner(self, row, col):
       
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - i * dr, col - i * dc
                if 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

    def on_click(self, event):
        if self.message.cget("text").startswith("Player"):
            col = event.x // 80
            for row in range(ROWS - 1, -1, -1):
                if self.board[row][col] == EMPTY:
                    self.board[row][col] = self.current_player
                    self.draw_board()
                    if self.check_winner(row, col):
                        self.message.config(text=f"Player {self.current_player} wins!")
                        self.canvas.unbind("<Button-1>")
                    else:
                        self.current_player = PLAYER2 if self.current_player == PLAYER1 else PLAYER1
                        self.message.config(text=f"Player {self.current_player}'s turn")
                    break

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = ConnectFour()
    game.start()
