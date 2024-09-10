import os

def create_chocolate_bar(rows, cols):
    if rows <= 0 or cols <= 0:
        return None
    
    chocolate_bar = []
    for i in range(1, rows + 1):
        row = []

        for j in range(1, cols + 1):
            if i == 1 and j == 1:
                row.append("P")
            else:
                row.append(f"{i}{j}")

        chocolate_bar.append(row)

    return chocolate_bar


def print_chocolate_bar(chocolate_bar):
    if chocolate_bar is None:
        print(None)
        return
    
    for row in chocolate_bar:
        print("\t".join(row))


def clear_and_print(chocolate_bar):
    os.system("cls" if os.name == "nt" else "clear")
    print_chocolate_bar(chocolate_bar)


def eat_chocolate_bar(chocolate_bar, row, col):
    # Check if the chocolate bar is None
    if chocolate_bar is None:
        return None
    
    # Check if the input is within the grid
    if row < 1 or row > len(chocolate_bar) or col < 1 or col > len(chocolate_bar[0]):
        return None
    
    # Eat the chocolate bar
    for i in range(row - 1, len(chocolate_bar)):
        for j in range(col - 1, len(chocolate_bar[i])):
            chocolate_bar[i][j] = " " 
    
    return chocolate_bar


def ask_cell_number(chocolate_bar):
    while True:
        try:
            y = int(input("Enter the row number: "))
            x = int(input("Enter the column number: "))
        except ValueError: 
            clear_and_print(chocolate_bar)
            print("Invalid input. Please enter numeric values for row and column.")
            continue 

        # Check if the input is within the grid
        if y < 1 or y > len(chocolate_bar) or x < 1 or x > len(chocolate_bar[0]):
            clear_and_print(chocolate_bar)
            print("Invalid input. Please choose a row and column within the grid.")
            continue
        
        # Check if the block has already been eaten
        if chocolate_bar[y - 1][x - 1] == " ":
            clear_and_print(chocolate_bar)
            print("That block has already been eaten. Please choose another block.")
            continue
        
        return y, x  


def check_winners(chocolate_bar):
    if chocolate_bar is None:
        return None

    # Check if the top left block is the only block left
    for row in chocolate_bar:
        for cell in row:
            if cell != " ":
                return False

    return True


def game():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create the chocolate bar
    chocolate_bar = create_chocolate_bar(rows, cols)
    clear_and_print(chocolate_bar)
    
    while not check_winners(chocolate_bar):

        # Set row and col from input
        row, col = ask_cell_number(chocolate_bar)

        # Eat the chocolate bar
        chocolate_bar = eat_chocolate_bar(chocolate_bar, row, col)
        clear_and_print(chocolate_bar)

    print("You lose!")


if __name__ == "__main__":
    game()