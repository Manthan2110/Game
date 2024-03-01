import random

computer = random.randint(1,100)
print(computer)
status = True
while status:
    user_choice = int(input("Enter your guess:"))
    if user_choice> computer:
        print("HINT : Guess lower Number")
    elif user_choice < computer:
        print("HINT : Guess the upper number")
    else:
        print("YOU WIN !!!")
        status=False