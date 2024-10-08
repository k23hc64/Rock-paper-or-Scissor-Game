import random

while True:      

      choicess = ['rock','paper','scissors']
    computer = random.choice(choicess)
    
    player = None
    while player not in choicess:
        player = input("rock or paper or scissors?:")

    if computer == "rock":
        if player == "rock":
            print("computer:" + computer)
            print("player:" + player)
            print("Tie")
        elif player == "paper":
            print("computer:" + computer)
            print("player:" + player)
            print("you won")
        else:
            print("computer:" + computer)
            print("player:" + player)
            print("you lose")
    elif computer == "paper":
        if player == "rock":
            print("computer:" + computer)
            print("player:" + player)
            print("you lose!")
        elif player == "paper":
            print("computer:" + computer)
            print("player:" + player)
            print("Tie")
        else:
            print("computer:" + computer)
            print("player:" + player)
            print("you Won!!")
    else:
        if player == "rock":
            print("computer:" + computer)
            print("player:" + player)
            print("you won")
        elif player == "paper":
            print("computer:" + computer)
            print("player:" + player)
            print("you lose")
        else:
            print("computer:" + computer)
            print("player:" + player)
            print("Tie!!")

    play_again = input("do you want to play again? yes/no").lower()
    if play_again != "yes":
        break
        
print("Bye")







