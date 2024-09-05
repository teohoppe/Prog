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
eaten = []

def eat_chocolate_bar(chocolate_bar, row, col):
    if chocolate_bar is None:
        return None
    
    if row < 1 or row > len(chocolate_bar) or col < 1 or col > len(chocolate_bar[0]):
        return None
    
    for i in range(row - 1, len(chocolate_bar)):
        for j in range(col - 1, len(chocolate_bar[i])):
            eaten.append(chocolate_bar[i][j])
            chocolate_bar[i][j] = " "
            print(eaten)
            # Fixa så att dem raderas helt 

    return chocolate_bar


def ask_cell_number(chocolate_bar):

    try:
        y = int(input("Enter the row number: "))
        x = int(input("Enter the column number: "))
    except ValueError: 
        print("Invalid input. Please enter a valid row and column.")
        return ask_cell_number(chocolate_bar)
    
    if x > len(chocolate_bar) or y > len(chocolate_bar):
        print("Invalid input. Please enter a valid row and column.")
        return ask_cell_number(chocolate_bar)
    
    if x in eaten and y in eaten:
        print("Invalid input. Please enter a valid row and column.")
        return ask_cell_number(chocolate_bar)

    return y, x


def check_winners(chocolate_bar):
    if chocolate_bar is None:
        return None

    for row in chocolate_bar:
        for cell in row:
            if cell != " ":
                return False

    return True


def game():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    chocolate_bar = create_chocolate_bar(rows, cols)
    print_chocolate_bar(chocolate_bar)
    
    while not check_winners(chocolate_bar):

        # Set row and col from input
        row, col = ask_cell_number(chocolate_bar)

        # Eat the chocolate bar
        chocolate_bar = eat_chocolate_bar(chocolate_bar, row, col)
        print_chocolate_bar(chocolate_bar)

    print("You lose!")


if __name__ == "__main__":
    game()