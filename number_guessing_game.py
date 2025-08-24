import random 
number_guess = random.randint(1, 100)

while True: 
    try:
        number_guess_input = input("Welcome to a guessing number game so please enter a number from 0 to 100: ") 
        if number_guess_input < number_guess: 
            print("The number {number_guess_input} is too low please enter a higher number.") 
        elif number_guess_input > number_guess: 
            print("The number {number_guess_input} is too high please enter a lower number.") 
        else: 
            print("Congratulations! The number {number_guess_input} is the guessing number.")
    except ValueError: 
        print("Please enter a valid number!")
        