# # Building Hangman Game
# import random
# print ("WELCOME TO HANGMAN GAME")

# word_list = ['camel', 'cow', 'buffallo', 'dinosaur', 'aardvark']
# chosen_word = random.choice(word_list)
# print(chosen_word)
# # to print '_" for each letter in the word
# place_holder = ""
# blank = (len(chosen_word))
# for letter in range (1,blank + 1):
#     place_holder += " _"
# print(place_holder)
# #given the lives to player
# lives = 5
# print("You have 5 lives")
# # to check if the letter is in the word
# correct_letters=[]
# condition = True
# while condition == True:
    
#     guess = str(input("Guess the letter : ").lower())
#     display = ''
#     answer = []
#     for i in chosen_word:
#          if i == guess:
#             display += i
#             correct_letters.append(i)
#          elif i in correct_letters:
#             display += i
#          else :
#             display += '_'
#     print(display)                  
#     if guess not in  chosen_word :
#          lives -= 1
#          if lives == 0:
#                 print("You lose")
#                 condition = False
        
        
#     # To check the result of the game
#     if "_" not in display:
#         print("You win")
#         condition = False

        


import random

# List of words to choose from
words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

# Function to start the game
def start_game():
    word = random.choice(words)
    word_length = len(word)
    guesses = ''
    attempts = word_length + 2  # Number of attempts the player gets

    print("The word has", word_length, "letters.")
    
    while attempts > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        
        if failed == 0:
            print("\nYou won!")
            break
        
        guess = input("\nGuess a letter: ")
        guesses += guess
        
        if guess not in word:
            attempts -= 1
            print("Wrong guess. You have", attempts, "attempts left.")
        
        if attempts == 0:
            print("\nYou lost. The word was", word)

if __name__ == "__main__":
    start_game()
