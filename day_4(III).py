#  Rock, Paper, Scissors Game
import random
print ("Welcome to the Rock, Paper, Scissors game!")
print("Enter your choice Rock, Paper or Scissor, write 0 for Rock, 1 for Paper and 2 for Scissor")

user_choice = int(input("Enter your choice : "))   #taking choice from the user

# assigning user choice to its respective value
if user_choice == 0:
    print("You choose rock")
elif user_choice==1 :
    print("You choose paper")
elif user_choice==2 :
    print("You choose scissor")
else:
    print("Invalid choice")

computer_choice = random.randint(0,2)  #computer choice

# assigning computer choice to its respective value
if computer_choice == 0:
    print("Computer choose rock")
elif computer_choice==1 :
    print("Computer choose paper")
elif computer_choice==2 :
    print("Computer choose scissor")

#defining the rules of the game
if computer_choice == user_choice:
    print("It's a tie")
elif computer_choice == 0 and user_choice == 1:
    print("You win")
elif computer_choice==1 and user_choice == 2:
    print("You win")
elif computer_choice==2 and user_choice == 0:
    print("You win")
else:
    print("You lose")