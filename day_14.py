# Building a higher & lower game
import random

data = [
    {
        "name" : "Lionel Messi",
        "follower_count" : 101,
        "description" : "Footballer",
        "country" : "Argentina"

    },
    {
        "name" : "Selena Gomez",
        "follower_count" : 399,
        "description" : "Musician & Actress",   
        "country" : "USA"
    } ,
    {
        "name" : "Cristiano Ronaldo",
        "follower_count" : 500,
        "description" : "Footballer",
        "country" : "Portugal"
    } , 
    {
        "name" : "Kylie Jenner",
        "follower_count" : 300,
        "description" : "Reality TV Star",
        "country" : "USA"
    }, 
    {
        "name" : "Kim Kardashian",
        "follower_count" : 400,
        "description" : "Reality TV Star",
        "country" : "USA"
    },
    {
        "name" : "Dwayne Johnson",
        "follower_count" : 200,
        "description" : "Actor & Wrestler",
        "country" : "USA"
    }
    ]

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
score = 0
repeat_game = True

account_b = random.choice(data)

while repeat_game == True:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")         

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        print("You are correct.")  
        score += 1
        print(f"Your score is {score}.")  
    else:
        print("Sorry, that's wrong.")
        print(f"Your score is {score}.")
        repeat_game = False
print("Game over.")