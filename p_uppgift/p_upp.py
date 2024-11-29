# Teo Hoppe
# 2024-11-29
import time
import operator 
import os

class Trollgame:
    def __init__(self):
        
        self.board = []
        self.position = []
        
        self.boardsize = 0
        self.time = 0
        self.trolls = 0

        self.file = "p_uppgift/scores.txt"

    def start_game(self):
        self.clear_screen()
        self.rules()
        self.get_boardsize()
        self.play_game()

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
                    self.board = [["-" for _ in range(size)] for _ in range(size)] # Create the board (matrix)
                    break
                else:
                    print("Board size must be at least 4x4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.clear_screen()
    
    def print_board(self):
        """Print the current board state."""
 
        print("┌" + "─" * (2 * self.boardsize - 1) + "┐") # Custom corners for the board
        for row in self.board:
            print("│" + "│".join(row) + "│")              # Custom sides for the board
        print("└" + "─" * (2 * self.boardsize - 1) + "┘") # Custom corners for the board
        print()

    def place_troll(self, row, col):
        """Place a troll on the board at the given column."""

        self.board[row][col] = "*"
        self.position.append((row, col))
        self.trolls += 1

    def remove_troll(self):
        """Remove the troll from the given row."""

        try:
            row, col = self.position.pop()
            self.board[row][col] = "-"
            self.trolls -= 1
        except IndexError:
            print("No trolls to remove.")

    def is_valid_position(self, row, col):
        """Check if the troll can be placed on the board without being on the same diagonal or column as another troll."""

        for check_r, check_c in self.position: # Iterate over the existing trolls

            # Check if the troll is on the same diagonal or column as another troll
            if abs(row - check_r) == abs(col - check_c) or row == check_r or col == check_c:
                return False
        return True

    def save_score(self, elapsed_time):
        """Save the score to the scores file."""

        score_entry = f"{self.boardsize}x{self.boardsize} - {elapsed_time:.2f} seconds\n"
        scores = self.load_scores()

        # Add new score entry and sort based on board size and time
        scores.append((self.boardsize, elapsed_time, score_entry))
    
        scores = sorted(scores, key=operator.itemgetter(1))               # Sort by time
        scores = sorted(scores, key=operator.itemgetter(0), reverse=True) # Sort by board size in descending order  

        # Write sorted scores back to file
        with open(self.file, "w") as file:
            for _, _, entry in scores:  # Iterate over the sorted scores
                file.write(entry)       # Write the score entry string to the file
        print("Highscore saved!")

    def load_scores(self):
        """Load the scores from the scores file."""

        scores = []
        if os.path.exists(self.file):                        # Check if the file exists
            with open(self.file, "r") as file:
                for line in file:
                    parts = line.strip().split(" - ")
                    if len(parts) == 2:                          # Ensure line has exactly two parts
                        try:
                            size = int(parts[0].split("x")[0])   # Extract the board size
                            time = float(parts[1].split()[0])    # Extract the time
                            scores.append((size, time, line))
                        except ValueError:
                            print(f"Skipping malformed line: {line.strip()}")
        return scores

    def show_scores(self):
        """Show the scores from the scores file."""

        try: 
            with open(self.file, "r") as file:
                print("Scores:")
                print(file.read())
        except IOError:     # IF FILE NOT FOUND
            print("Error reading scores.")    
    
    def end_game(self):
        """End the game and show the elapsed time."""

        self.print_board()
        end_time = time.time()
        elapsed_time = end_time - self.time

        print("Congratulations! You have placed all the trolls.")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

        self.save_score(elapsed_time)
        self.show_scores()             

    def play_game(self):
        """Play the game."""

        self.time = time.time() # Start the timer
        self.trolls = 0 # Reset the number of trolls
        self.position = [] # Reset the position list
        
        while self.trolls != self.boardsize:
            row = self.trolls
            self.print_board()
            try:
                place = input(f"Place troll {row + 1} choose colume between 1-{self.boardsize} or 'undo'or 'break' to quit: ")

                # Check if the user wants to undo the last move
                if place.lower() == "undo":
                    if row == 0:
                        print("Cannot undo the first move.")
                        continue
                    self.remove_troll()
                    continue
                elif place.lower() == "break":
                    break
                
                col = int(place) - 1
                
                # Check if the column is within the board size
                if any(existing_col == col for _, existing_col in self.position):
                    print("Troll cannot be placed in the same column as another troll.")
                    continue

                # Check if the column is within the board size
                if col < 0 or col >= self.boardsize:
                    raise ValueError
                else:
                    if self.is_valid_position(row, col):
                        self.place_troll(row, col)
                        continue
                    else:
                        print("Troll cannot be placed on the same diagonal.")

            except ValueError:
                print("Invalid input. Please enter a valid numer or 'undo'.")
                continue

        if self.trolls == self.boardsize:
            self.end_game()


# An algorithm that plays the Trollgame
class TrollgameAI(Trollgame): # Inherit from Trollgame      
    def __init__(self):     
        super().__init__() # Call the constructor of the parent class

    def start(self):
        self.rules()
        self.get_boardsize()
        self.play_game()

    # Override the play_game method
    def play_game(self):    
        """Play the game automatically using a backtracking algorithm."""

        self.time = time.time()
        if self.solve(0):
            self.end_game()
        else:
            print("No solution found.")
    
    def solve(self, row):
        """Use backtracking to place trolls on the board."""

        if row == self.boardsize:           # Error handling
            return True

        # Try to place a troll in each column of the current row 
        for col in range(self.boardsize):
            if self.is_safe(row, col):
                self.place_troll(row, col)

                if self.solve(row + 1):
                    return True
                self.remove_troll()

        return False

    def is_safe(self, row, col):
        """Check if it's safe to place a troll at (row, col)."""

        for check_r, check_c in self.position: # Iterate over the existing trolls
            # Check if the troll is in the same column or diagonal as another troll
            if check_c == col or abs(row - check_r) == abs(col - check_c): 
                return False
        return True


def main():
    game = Trollgame()
    while True:
        try:
            choice = int(input("1. Play game\n2. Show scores\n3. Let AI play\n4. Exit\nEnter choice: "))
            if choice == 1:
                game.start_game()

            elif choice == 2:
                game.show_scores()

            elif choice == 3:
                game = TrollgameAI()
                game.start()

            elif choice == 4:
                break
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()