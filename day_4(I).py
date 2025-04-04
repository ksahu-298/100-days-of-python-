# Day 4 - Coin Toss Game
# This is a simple game where the user has to guess whether the coin will land on heads or tails.
import random
print ("Choose what do you want Heads / Tails ?")
coin_choice = input("Enter Heads for Heads & Tails for Tails : ")
a=random.randint(1,3)

if a==1:
    print("Heads")
else:
    print("Tails")

if coin_choice == a:
    print("You Win")
else:
    print("You Lose")
