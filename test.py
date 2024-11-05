import time
import os
import tkinter as tk
from tkinter import messagebox

class TrollGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arga Troll Spelet")
        
        self.start_time = 0
        self.board_size = 0
        self.board = []
        self.positions = []
        
        self.setup_game()

    def setup_game(self):
        self.intro_label = tk.Label(self.root, text="Välkommen till Arga Troll Spelet!\nVälj storlek på brädet (minst 4x4):")
        self.intro_label.pack()

        self.size_entry = tk.Entry(self.root)
        self.size_entry.pack()

        self.start_button = tk.Button(self.root, text="Starta spel", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        try:
            size = int(self.size_entry.get())
            if size >= 4:
                self.board_size = size
                self.positions = []
                self.board = [['_' for _ in range(size)] for _ in range(size)]
                
                self.intro_label.pack_forget()
                self.size_entry.pack_forget()
                self.start_button.pack_forget()
                
                self.create_board()
                self.start_time = time.time()
            else:
                messagebox.showerror("Ogiltig storlek", "Brädet måste vara minst 4x4.")
        except ValueError:
            messagebox.showerror("Felaktig inmatning", "Ange ett giltigt heltal för storlek.")

    def create_board(self):
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                btn = tk.Button(self.board_frame, text='_', width=4, height=2,
                                command=lambda r=row, c=col: self.handle_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
        
        self.undo_button = tk.Button(self.root, text="Ångra", command=self.undo_move)
        self.undo_button.pack()

    def handle_click(self, row, col):
        if self.board[row][col] == '_':
            if self.is_valid_position(row, col):
                self.place_troll(row, col)
            else:
                messagebox.showwarning("Ogiltig placering", "Troll får inte placeras på samma rad, kolumn eller diagonal.")
        elif self.board[row][col] == '*':
            self.remove_troll(row, col)

        if len(self.positions) == self.board_size:
            self.end_game()

    def place_troll(self, row, col):
        self.board[row][col] = '*'
        self.positions.append((row, col))
        self.buttons[row][col].config(text='*')

    def remove_troll(self, row, col):
        self.board[row][col] = '_'
        self.positions.remove((row, col))
        self.buttons[row][col].config(text='_')

    def undo_move(self):
        if self.positions:
            row, col = self.positions.pop()
            self.board[row][col] = '_'
            self.buttons[row][col].config(text='_')
        else:
            messagebox.showinfo("Ingen ångring", "Det finns inget drag att ångra.")

    def is_valid_position(self, row, col):
        for r, c in self.positions:
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def end_game(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        messagebox.showinfo("Spelet över", f"Grattis! Du har placerat alla troll utan konflikter.\nTid: {elapsed_time:.2f} sekunder")
        self.save_score(elapsed_time)

    def save_score(self, elapsed_time):
        try:
            with open("highscores.txt", "a") as file:
                file.write(f"{self.board_size}x{self.board_size} - {elapsed_time:.2f} sekunder\n")
            messagebox.showinfo("Highscore", "Din tid har sparats!")
        except IOError:
            messagebox.showerror("Fel", "Kunde inte spara highscore.")

    def show_highscores(self):
        if os.path.exists("highscores.txt"):
            with open("highscores.txt", "r") as file:
                highscores = file.read()
            messagebox.showinfo("Highscores", highscores)
        else:
            messagebox.showinfo("Highscores", "Inga highscores sparade.")

if __name__ == "__main__":
    root = tk.Tk()
    game = TrollGameGUI(root)
    root.mainloop()