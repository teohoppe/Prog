import time
import os

class Trollgame:
    def __init__(self):
        self.boardsize = 0
        self.board = []
        self.position = []
        self.time = 0
        self.trolls = 0


    def rules(self):
        print("Welcome to the Troll Game!")
        print("Rules:")
        print("1. One troll per row.")
        print("2. One troll per column.")
        print("3. No trolls on the same diagonal.")
        print("Use 'undo' to undo the last move.")


    def get_boardsize(self):
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
        print("┌" + "─" * (2 * self.boardsize - 1) + "┐")
        for row in self.board:
            print("│" + "│".join(row) + "│")
        print("└" + "─" * (2 * self.boardsize - 1) + "┘")
        print()


    def place_troll(self, row, col):
        self.board[row][col] = "*"
        self.position.append((row, col))
        self.trolls += 1


    def remove_troll(self, row, col):
        row, col = self.position.pop()
        self.board[row][col] = "-"
        self.trolls -= 1


    def check_diagonal(self, row, col):
        for r, c in self.position:
            if abs(row - r) == abs(col - c):
                return False
        return True
    

    def save_score(self, elapsed_time):
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            for i, score in enumerate(scores):
                if float(score) > elapsed_time:
                    scores.insert(i, str(elapsed_time) + "\n")
                    break
            else:
                scores.append(str(elapsed_time) + "\n")
        with open("scores.txt", "w") as file:
            file.writelines(scores)
            

    

    def show_scores(self):
        try: 
            with open("scores.txt", "r") as file:
                print("Scores:")
                print(file.read())
        except IOError:
            print("Error reading scores.")

    
    def play_game(self):
        self.time = time.time()
        while self.trolls != self.boardsize:
            for row in range(self.boardsize):
                while True:
                    self.print_board()
                    try:
                        place = input(f"Place troll {row + 1} choose colume between 1-{self.boardsize} or 'undo': ")

                        if place.lower() == "undo":
                            if row == 0:
                                print("Cannot undo the first move.")
                                continue
                            self.remove_troll(row, 0)
                            row -= 1
                            break
                        
                        col = int(place) - 1
                        if col < 0 or col >= self.boardsize:
                            raise ValueError
                        else:
                            if self.check_diagonal(row, col):
                                self.place_troll(row, col)
                                break
                            else:
                                print("Troll cannot be placed on the same diagonal.")

                    except ValueError:
                        print("Invalid input. Please enter a valid numer or 'undo'.")
                        continue
        self.end_game()
        

    def end_game(self):
        self.print_board()
        end_time = time.time()
        elapsed_time = end_time - self.time
        print("Congratulations! You have placed all the trolls.")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        self.save_score(elapsed_time)
        self.show_scores()


    def main(self):
        self.rules()
        self.get_boardsize()
        self.play_game()

if __name__ == "__main__":
    game = Trollgame()
    game.main()                