# Đầu tiên là yêu cầu người ta nhập 'rock', 'paper', 'scissors' để bắt đầu game chơi kéo - búa - bao 
# Rồi thiết lập một cho máy để chọn kéo - búa - bao một cách ngẫu nhiên để đấu với người chơi
# Khi đã có kết quả rồi thì yêu cầu người chơi có muốn chơi tiếp không bằng 'yes', 'no' 
# nếu người chơi nhập 'no' thì trò chơi kết thúc nhưng khi nhập 'yes' thì trò chơi được tiếp tục 

import random 

# Chúng ta sẽ xài dictionary để có thể vừa nhập từ khóa vừa gắn luôn giá trị mà ta sẽ gán trực tiếp vào từ khóa phía trước
rock_paper_scissors_emoji = {'rock': '👊', 'paper': '🖐', 'scissors': '✌'} 
choice = tuple(rock_paper_scissors_emoji.keys()) 
computer_choice = random.choice(choice)

def rock_paper_scissors_input(): 
    while True:
        player_choice = input("Rock, Paper, Scissors? (enter 'rock', 'paper', 'scissors' to start the game): ")
        if player_choice in choice: 
            return player_choice
        else: 
            print(f"You can't not enter '{player_choice}' and you can only enter 'rock', 'paper', 'scissors' to start the game") 
            continue

def display_choice(player_choice, computer_choice):
    print(f"Computer chose {computer_choice} {rock_paper_scissors_emoji[computer_choice]}") 
    print(f"You chose {player_choice} {rock_paper_scissors_emoji[player_choice]}") 
def checking_the_result_game(player_choice, computer_choice): 
    if player_choice == computer_choice: 
        print(f"The result is a DRAW!")
    # Player lose
    elif (
        (player_choice == 'rock' and computer_choice == 'paper') or 
        (player_choice == 'paper' and computer_choice == 'scissors') or 
        (player_choice == 'scissors' and computer_choice == 'rock')): 
        
        print("You lose and computer won!")
    # Computer lose 
    elif (
        (player_choice == 'paper' and computer_choice == 'rock') or 
        (player_choice == 'scissors' and computer_choice == 'paper') or 
        (player_choice == 'rock' and computer_choice == 'scissors')): 

        print("You won and computer lose!") 
def ask_player_wanna_continue_play(): 
    while True: 
        game_continue = input("Wanna continue? (enter 'yes', 'no' to answer): ") 
        if game_continue == 'no': 
            break 
        
        else: 
            print(f"You can't type '{game_continue}' to restart or stop the game so you need to type 'yes' for continue playing and 'no' for stop playing.")
            continue

def play_game():
    while True: 
        player_choice = rock_paper_scissors_input() 
        
        
        display_choice(player_choice, computer_choice) 
        checking_the_result_game(player_choice,  computer_choice) 
        
        continue_play = True 
        while continue_play: 
            game_continue = input("Wanna continue? (enter 'yes', 'no' to answer): ") 
            if game_continue == 'no': 
                break 
            elif game_continue == 'yes': 
                continue_play = False
            else: 
                print(f"You can't type '{game_continue}' to restart or stop the game so you need to type 'yes' for continue playing and 'no' for stop playing.")
                continue
        
play_game()


    

