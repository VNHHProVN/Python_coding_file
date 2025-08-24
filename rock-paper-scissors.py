# Đầu tiên là yêu cầu người ta nhập 'rock', 'paper', 'scissors' để bắt đầu game chơi kéo - búa - bao 
# Rồi thiết lập một cho máy để chọn kéo - búa - bao một cách ngẫu nhiên để đấu với người chơi
# Khi đã có kết quả rồi thì yêu cầu người chơi có muốn chơi tiếp không bằng 'yes', 'no' 
# nếu người chơi nhập 'no' thì trò chơi kết thúc nhưng khi nhập 'yes' thì trò chơi được tiếp tục 

import random 

# Chúng ta sẽ xài dictionary để có thể vừa nhập từ khóa vừa gắn luôn giá trị mà ta sẽ gán trực tiếp vào từ khóa phía trước
rock_paper_scissors_emoji = {'rock': '👊', 'paper': '🖐', 'scissors': '✌'} 
computer_choice = random.choice('rock', 'paper', 'scissors') 

while True: 
    rock_paper_scissors_input = input("Wanna play rock, paper, scissors and enter each word (rock), (paper), (scissors) to play: ") 
    if rock_paper_scissors_input not in rock_paper_scissors_emoji: 
        print("Please try again and enter (rock), (paper), (scissors)") 
        continue 
    