from random import randint

computer_choice = randint(1, 100)
print("Welcome to the Number Guessing Game!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def guess_number(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        number = int(input("Guess a number between 1 and 100: "))
        
        if number == computer_choice:
            print("You got it! 🎉")
            return
        elif number < computer_choice:
            print("Too low.")
        else:
            print("Too high.")
        
        attempts -= 1

    print(f"Sorry, you're out of attempts. The number was {computer_choice} 😢")

if difficulty == "easy":
    guess_number(10)
elif difficulty == "hard":
    guess_number(5)
else:
    print("Invalid input. Please choose 'easy' or 'hard'.")

print("Thanks for playing!")