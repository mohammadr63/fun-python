import random

name = input("please enter your name ?  ")

opponent = input("please enter you opponent name ?")


print("rock.....paper.....scissor")

lap = int(input("please enter the lap"))

for num in range(1,lap+1):
    player = input("please retrun you choise ? >>")
    number = random.randint(1,3)
    if number == 1 :
        computer = "rock"
        print(opponent , "chois rock")
    elif number == 2:
        computer = "paper"
        print(opponent , "chois paper")
    elif number == 3 :
        computer = "scissor"
        print(opponent , "chois scissor")
    if computer == "rock" and player == "paper" :
        print(name,"wine")
    elif  computer == "rock" and player == "scissor" :
        print(opponent , "wine")
    elif computer == "paper" and player == "rock" :
        print(opponent , "wine")
    elif computer == "paper" and player == "scissor" :
        print(name, "wine")
    elif computer == "scissor" and player == "paper" :
        print(opponent, "wine")
    elif computer == "scissor" and player == "rock" :
        print(name ,"wine")
    else :
        print("qule")