from tv import TV
import os

filename = "C:/Users/teoho/Prog/prgob24lab1/tvs.txt" # File path 

def read_file(filename):
    """Reads a file and returns a list of TV objects"""

    tv_list = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
                tv_name = data[0]
                max_channel = int(data[1])
                current_channel = int(data[2])
                max_volume = int(data[3])
                current_volume = int(data[4])
                tv = TV(tv_name, max_channel, current_channel, max_volume, current_volume)
                tv_list.append(tv)

    except FileNotFoundError:
        print("File not found")
    
    return tv_list


def write_file(filename, tv_list):
    """Writes a list of TV objects to a file"""

    with open(filename, "w", encoding="utf-8") as file:
        for tv in tv_list:
            file.write(tv.str_for_file() + "\n")


def clear_screen():
    """Clears the terminal screen"""

    os.system("cls" if os.name == "nt" else "clear")


def adjust_TV_menu():
    """Prints the menu for adjusting the TV and returns the user's choice"""

    print("1. Volume up")
    print("2. Volume down")
    print("3. Change channel")
    print("4. Exit")
    
    while True:
        try:
            sub_choice2 = int(input("Choice: "))
            if 1 <= sub_choice2 <= 4:
                return sub_choice2
            else:
                print("Invalid choice, please select between 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        

def change_channel(tv):
    """Changes the channel of the TV"""

    # Error handling for invalid input
    try:
        new_channel = int(input("Enter channel: "))
        tv.change_channel(new_channel)
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    tv_list = read_file(filename)

    if not tv_list:
        print("No TVs found")
        return
    
    while True:
        # Print the main menu
        print("***Welcome to the TV simulation***")
        for i, tv in enumerate(tv_list):
            print(f"{i+1}. {tv.tv_name}")
        print(f"{len(tv_list)+1}. Exit")

    
        try:    
            choice = int(input("Choice: "))
            if choice == len(tv_list) + 1:
                break
            if not 1 <= choice <= len(tv_list):
                raise ValueError
        except ValueError:
            print("Invalid choice")
            continue
        clear_screen()
        tv = tv_list[choice-1]

        # Submenu for adjusting the TV
        while True:
            print(tv, end="\n")
            sub_choice = adjust_TV_menu()
            if sub_choice == 1:
                clear_screen()
                tv.volume_up()
            elif sub_choice == 2:
                clear_screen()
                tv.volume_down()
            elif sub_choice == 3:
                clear_screen()
                change_channel(tv)
            elif sub_choice == 4:
                clear_screen()
                break


    write_file(filename, tv_list)
    print("Exiting simulation\n")

        
if __name__ == "__main__":
    main()