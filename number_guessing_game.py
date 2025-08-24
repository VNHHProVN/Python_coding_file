import random 
number_guess = random.randint(0, 100)

while True: 
    try:
        number_guess_input = int(input("Chào mừng đến với trò chơi đoán số và hãy nhập một con số từ 0 đến 100: "))
        if number_guess_input < number_guess: 
            print(f"Con số {number_guess_input} quá nhỏ hãy nhập một con số lớn hơn.") 
        elif number_guess_input > number_guess: 
             print(f"Con số {number_guess_input} quá lớn hãy nhập một con số nhỏ hơn.") 
        else: 
            print(f"CHÚC MỪNG! Con số {number_guess_input} chính là con số chính xác.") 
            break
    except ValueError: 
        print("Vui lòng hãy nhập một số nguyên từ 0 đến 100!")
        