import random
import os

# List to store the results of the dices
dice_result = []

# Ask the user how many dices they want to roll and how many throws each player gets
amount = int(input("How many dices do you want to roll? "))
throws = int(input("How many throws do each player get? "))

while True:
    # Clear the list after each round
    dice_result.clear()
    
    start = input("Throw the dices by pressing enter or exit by typing 'A'")

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    if start == "A":
        break
    else:
        # Loop through the amount of throws the user wants
        for n in range(0, throws):
            print(f"Throw {n + 1}")

            # Loop through the amount of dices the user wants
            for i in range(0, amount):
                roll = random.randint(1, 6)
                print(f"Dice {i + 1}: {roll}")
                dice_result.append(roll) # Append the result to the list

            print()
        
        # Print the results of the dices
        print(f"Results: {dice_result}")