# Teo Hoppe
# 2024-11-12
import time, operator, os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class TrollgameGUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Trollgame")

        self.boardsize = 0
        self.position = []
        self.trolls = 0

    def setup_game(self):
        self.rules()

        self.intro_label = Label(self.root, text="Welcome to the Trollgame!\nPleases select the board size(at least 4x4):")
        self.intro_label.pack()

        self.boardsize_entry = Entry(self.root)
        self.boardsize_entry.pack()

        self.submit_button = Button(self.root, text="Submit", command=self.start_game)
        self.submit_button.pack()

        # self.score_button = Button(self.root, text="Show scores", command=self.show_scores)
        # self.score_button.pack()

    def rules(self):
        self.rules_label = Label(self.root, text="Rules:\n1. One troll per row.\n2. One troll per column.\n3. No trolls on the same diagonal.")
        self.rules_label.pack()

    def start_game(self):
        try:
            size = int(self.boardsize_entry.get())
            if size >= 4:
                self.boardsize = size
                self.position = []
                self.board = [["_" for _ in range(size)] for _ in range(size)]

                self.intro_label.pack_forget()
                self.boardsize_entry.pack_forget()
                self.submit_button.pack_forget()
                self.rules_label.pack_forget()


                self.create_board()
                self.time = time.time()
            else:
                messagebox.showerror("Error", "Board size must be at least 4x4.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def create_board(self):
        self.buttons = [[None for _ in range(self.boardsize)] for _ in range(self.boardsize)]
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for row in range(self.boardsize):
            for col in range(self.boardsize):
                button = Button(self.frame, text="_", width=4, height=2, command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        print("1")
        if self.board[row][col] == "_":
            print("2")
            if self.is_vaild_position(row, col):
                print("3")
                self.place_troll(row, col)
                self.buttons[row][col].config(bg="green")
            else:
                messagebox.showerror("Error", "Invalid position.")
        elif self.board[row][col] == "*":
            self.remove_troll(row, col)
            self.buttons[row][col].config(bg="white")

        if len(self.position) == self.boardsize:
            self.end_game()

    def is_vaild_position(self, row, col):
        for check_r, check_c in self.position:
            if abs(row - check_r) == abs(col - check_c) or row == check_r or col == check_c:
                return False
        return True
    
    def place_troll(self, row, col):
        self.board[row][col] = "*"
        self.position.append((row, col))
        self.trolls += 1
        self.buttons[row][col].config(text="*")

    def remove_troll(self, row, col):
        if self.position:
            row, col = self.position.pop()
            self.board[row][col] = "_"
            self.trolls -= 1
            self.buttons[row][col].config(text="_")

    def end_game(self):
        end_time = time.time()
        time_elapsed = end_time - self.time
        messagebox.showinfo(f"Congratulations!",f"You have placed all the trolls in {time_elapsed:.2f} seconds.")
        
        self.save_score(time_elapsed)
        self.show_scores()

    def save_score(self, elapsed_time):
        """Save the score to the scores file."""

        score_entry = f"{self.boardsize}x{self.boardsize} - {elapsed_time:.2f} seconds\n"
        scores = self.load_scores()

        # Add new score entry and sort based on board size and time
        scores.append((self.boardsize, elapsed_time, score_entry))
    
        scores = sorted(scores, key=operator.itemgetter(1))  # Sort by time
        scores = sorted(scores, key=operator.itemgetter(0), reverse=True) # Sort by board size in descending order  

        # Write sorted scores back to file
        with open("scores.txt", "w") as file:
            for _, _, entry in scores:
                file.write(entry)  # Write the score entry string to the file
        print("Highscore saved!")

    def load_scores(self):
        """Load the scores from the scores file."""

        scores = []
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(" - ")
                    if len(parts) == 2:  # Ensure line has exactly two parts
                        try:
                            size = int(parts[0].split("x")[0])  # Extract the board size
                            time = float(parts[1].split()[0])    # Extract the time
                            scores.append((size, time, line))
                        except ValueError:
                            print(f"Skipping malformed line: {line.strip()}")
        return scores
        
    def restart_game(self):
        self.setup_game()
        self.frame.pack_forget()
        self.score_frame.pack_forget()
        self.score_label.pack_forget()
        self.play_again_button.pack_forget()
        self.rules_label.pack_forget()

    def show_scores(self):
        try:
            self.frame.pack_forget()
        except AttributeError:
            pass
        
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack()

        self.play_again_button = Button(self.score_frame, text="Play again", command=self.restart_game)
        self.play_again_button.pack()

        self.score_label = Label(self.score_frame, text="Scores:")
        self.score_label.pack()

        try:
            with open("scores.txt", "r") as file:
                scores = "\n".join(file.read().splitlines()[:10])
                self.score_label = Label(self.score_frame, text=scores)
                self.score_label.pack()
        except IOError:
            messagebox.showerror("Error", "Error reading scores.")


if __name__ == "__main__":
    root = tk.Tk()
    game = TrollgameGUI(root)
    game.setup_game()
    root.mainloop()