import random 

computer_decision = ['✌', '👊', '🖐'] 
computer_final_decision = random.choice(computer_decision) 

while True: 

    try: 
        player_decision_input = input("Paper, rock or scissors [enter 'p' for 'paper', 'r' for rock, 's' for scissors]: ").lower() 
        # Player choosen paper
        if player_decision_input == "p": 
            if computer_final_decision == "✌": 
                print(f"Computer chose {computer_final_decision}")
                print(f"But you chose {computer_decision[2]} so you lose.") 
                ask_player_want_to_continue = input("Wanna continue? (enter 'y' for yes or 'n' for no)").lower()
                if ask_player_want_to_continue == "y": 
                    continue
                if ask_player_want_to_continue == "no": 
                    break
            if computer_final_decision == "🖐": 
                print(f"Computer chose {computer_final_decision}")
                print(f"But you chose {computer_decision[2]} so the result is draw.")
                if ask_player_want_to_continue == "y": 
                    continue
                if ask_player_want_to_continue == "no": 
                    break 
            if computer_final_decision == "👊": 
                print(f"Computer chose {computer_final_decision}")
                print(f"But you chose {computer_decision[2]} so you won.")    
                if ask_player_want_to_continue == "y": 
                    continue
                if ask_player_want_to_continue == "no": 
                    break 
            # Player choose rock
            elif player_decision_input == "r": 
                if computer_final_decision == "✌": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[1]} so you won.") 
                    ask_player_want_to_continue = input("Wanna continue? (enter 'y' for yes or 'n' for no)").lower()
                    if ask_player_want_to_continue == "y": 
                        continue
                    if ask_player_want_to_continue == "no": 
                        break
                if computer_final_decision == "🖐": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[1]} so you lose.")
                    if ask_player_want_to_continue == "y": 
                        continue
                    if ask_player_want_to_continue == "no": 
                        break 
                if computer_final_decision == "👊": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[1]} so the result is a draw.")    
                if ask_player_want_to_continue == "y": 
                    continue
                if ask_player_want_to_continue == "no": 
                    break    
            # Player choose scissors 
            elif player_decision_input == "s": 
                if computer_final_decision == "✌": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[0]} so the result is a draw.") 
                    ask_player_want_to_continue = input("Wanna continue? (enter 'y' for yes or 'n' for no)").lower()
                    if ask_player_want_to_continue == "y": 
                        continue
                    if ask_player_want_to_continue == "no": 
                        break
                if computer_final_decision == "🖐": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[0]} so you won.")
                    if ask_player_want_to_continue == "y": 
                        continue
                    if ask_player_want_to_continue == "no": 
                        break 
                if computer_final_decision == "👊": 
                    print(f"Computer chose {computer_final_decision}")
                    print(f"But you chose {computer_decision[0]} so you lose.")    
                if ask_player_want_to_continue == "y": 
                    continue
                if ask_player_want_to_continue == "no": 
                    break

    except ValueError: 
        print("Please only enter 'r' (rock), 'p' paper), 's' (scissors)!")
