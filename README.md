# Game
This is Stone-Paper-Scissor Game
made by - Manthan Jadav
<br>
import random
game_list= ["stone", "paper", "scissor"]
computer = random.choice(game_list)

status = True
while status:
    user = input("Enter your choice:")
    if user == computer :
        print("TIE")
    elif user == "stone" and computer == "paper":
        print("computer won !!")
    elif user == "stone" and computer == "scissor":
        print("user won !!")
    elif user == "scisoor" and computer == "paper":
        print("user won !!")
    elif user == "scissor" and computer == "stone":
        print("computer won !!")
    elif user == "paper" and computer == "scissor":
        print("computer won !!")
    elif user == "paper" and computer == "stone":
        print("user won !!")
