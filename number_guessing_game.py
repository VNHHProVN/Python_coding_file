import random 
number_guess = random.randint(1, 100)
while True: 
    number_guess_input = input("Welcome to a guessing number game so please enter a number from 0 to 100: ")
    if number_guess == 10: 
        print(f"Congratulation number 10 is the correct number!") 
        break
    elif number_guess < 10: 
        print(f"You need enter a higher number because {number_guess_input} is too lower.")
    elif number_guess > 10: 
        print(f"You need to enter a lower number because {number_guess_input} is too high.") 
    elif number_guess < 0 or number_guess > 100: 
        print(f"You need to enter a number between 0 to 100!") 
    else: 
        print(f"The value {number_guess_input} is not a number so please try again and enter a number from 0 to 100!")