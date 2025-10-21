# Rock Paper scissors game
# """
# we are using the  random module method to randomly pick between a list [rock, paper, scissors]
# ask the user to pick [rock, papper, sicors] and check 
# if user picked rock and computer picked scissor rock beats scissor user wins
# if user picked rock and computer picked Paper Papper beats rock computer wins 
# if user picked scissors and computer picked Paper. scissors beats paper User wins
# if user picked paper and computer picked paper then it a draw
import random
run = True
user = input(" \n Enter your name: ")
print("Hello " + user )
while run:
    object = input("\n Pick an object(rock,paper,scissors): ")
    option = [ "rock", "paper", "scissors"]
    computer = random.choice(option)
    if object == "rock" and computer == "paper":
        print("\n computer WINS")
    elif object == "rock" and computer == "scissors":
        print(user ,"WINS")
    elif object == "rock" and computer == "rock":
        print("DRAW")
    elif object == "paper" and computer == "rock":
        print(user ,"WINS")
    elif object == "paper" and computer == "scissors":
        print("computer WINS")
    elif object == "paper" and computer == "paper":
        print("DRAW")
    elif object == "scissors" and computer == "scissors":
        print("DRAW")
    elif object == "scissors" and computer == "paper":
        print(user ,"WINS")
    elif object == "scissors" and computer == "rock":
        print("computer WINS")
    else:
        run = False
    


