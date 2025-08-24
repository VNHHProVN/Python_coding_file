# Đầu tiên lại ta phải đặt đầu vào của người dùng bên trong một cái while loop 
# Đầu vào là yêu cầu nhập "roll" để lăn 2 xúc xắc và gõ "stop" để dừng việc lăn xúc xắc
# Còn nếu người dùng không nhập 1 trong 2 từ "roll" với "stop" thì sẽ in ra báo lỗi 
import random

while True:
    choice = input("Do you want to roll 2 dices? (enter 'roll' for rolling 2 dices or enter 'stop' for stoping roll 2 dices): ").lower()
    if choice == "roll": 
        dice_number1 = random.randint(1,6)
        dice_number2 = random.randint(1,6) 
        print(f'The number one dice is roll {dice_number1}')
        print(f'The number two dice is roll {dice_number2}') 
    elif choice == "stop":
        print("Ok we will stop rolling the dice!") 
        break
    else: 
        print("Try again and you need to type 'roll' or 'stop'")