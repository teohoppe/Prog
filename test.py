import time
import operator
import os

class Trollgame:
    def __init__(self):
        self.boardsize = 0
        self.board = []
        self.position = []
        self.time = 0
        self.trolls = 0

    def clear_screen(self):
        """Clear the screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def rules(self):
        """Print the rules of the game."""
        print("Welcome to the Troll Game!")
        print("Rules:")
        print("1. One troll per row.")
        print("2. One troll per column.")
        print("3. No trolls on the same diagonal.")
        print("Use 'undo' to undo the last move.")

    def get_boardsize(self):
        """Get the board size from the user."""
        while True:
            try:
                size = int(input("Enter board size (at least 4x4): "))
                if size >= 4:
                    self.boardsize = size
                    self.board = [["-" for _ in range(size)] for _ in range(size)]
                    break
                else:
                    print("Board size must be at least 4x4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def print_board(self):
        """Print the current board state."""
        print("┌" + "─" * (2 * self.boardsize - 1) + "┐")
        for row in self.board:
            print("│" + "│".join(row) + "│")
        print("└" + "─" * (2 * self.boardsize - 1) + "┘")
        print()

    def place_troll(self, row, col):
        """Place a troll on the board at the given column."""
        self.board[row][col] = "*"
        self.position.append((row, col))
        self.trolls += 1

    def remove_troll(self):
        """Remove the most recent troll and return to the previous row."""
        if self.position:
            row, col = self.position.pop()
            self.board[row][col] = "-"
            self.trolls -= 1
            return row - 1  # Move back one row
        else:
            print("No trolls to remove.")
            return None

    def check_diagonal(self, row, col):
        """Check if the troll can be placed on the board without being on the same diagonal as another troll."""
        for r, c in self.position:
            if abs(row - r) == abs(col - c):
                return False
        return True

    def play_game(self):
        """Play the game."""
        self.time = time.time()
        row = 0  # Start with the first row

        while row < self.boardsize:
            self.print_board()
            try:
                action = input(f"Place troll in row {row + 1}, choose column between 1-{self.boardsize} or 'undo': ")

                if action.lower() == "undo":
                    if row == 0:
                        print("Cannot undo the first move.")
                    else:
                        row = self.remove_troll() or row  # Go back one row if undo is successful
                    continue

                # Place a troll in the specified column
                col = int(action) - 1
                if col < 0 or col >= self.boardsize:
                    raise ValueError("Invalid column")

                if self.check_diagonal(row, col):
                    self.place_troll(row, col)
                    row += 1  # Move to the next row
                else:
                    print("Troll cannot be placed on the same diagonal.")

            except ValueError:
                print("Invalid input. Please enter a valid number or 'undo'.")

        # End game if all trolls are placed successfully
        self.end_game()

    def end_game(self):
        """Display end-game information and save score."""
        self.print_board()
        end_time = time.time()
        elapsed_time = end_time - self.time
        print("Congratulations! You have placed all the trolls.")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        self.save_score(elapsed_time)
        self.show_scores()

    def save_score(self, elapsed_time):
        """Save the score to the scores file."""
        score_entry = f"{self.boardsize}x{self.boardsize} - {elapsed_time:.2f} seconds\n"
        scores = self.load_scores()
        scores.append((self.boardsize, elapsed_time, score_entry))

        # Sort by board size and time
        scores = sorted(scores, key=operator.itemgetter(1))
        scores = sorted(scores, key=operator.itemgetter(0), reverse=True)

        with open("scores.txt", "w") as file:
            for _, _, entry in scores:
                file.write(entry)
        print("Highscore saved!")

    def load_scores(self):
        """Load the scores from the scores file."""
        scores = []
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(" - ")
                    if len(parts) == 2:
                        try:
                            size = int(parts[0].split("x")[0])
                            time = float(parts[1].split()[0])
                            scores.append((size, time, line))
                        except ValueError:
                            print(f"Skipping malformed line: {line.strip()}")
        return scores

    def show_scores(self):
        """Show the scores from the scores file."""
        try:
            with open("scores.txt", "r") as file:
                print("Scores:")
                print(file.read())
        except IOError:
            print("Error reading scores.")

if __name__ == "__main__":
    game = Trollgame()
    game.rules()
    game.get_boardsize()
    game.play_game()