# creating a password generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','=','+']
print("Welcome to the Python Password Generator!")
ip_letters = int(input("How many letters would you like in your password? "))
ip_numbers = int(input("How many numbers would you like in your password? "))
ip_symbols = int(input("How many symbols would you like in your password? "))
ip_difficulty =(input("How difficult do you want your password to be? \n1.Easy \n2. Hard \n "))

easy_password = ""
hard_password = ""
# Easy password

if ip_difficulty == "Easy" or 1:
    for char in range (1,ip_letters + 1):
        password_letters= random.choice(letters)
        a= password_letters
        easy_password += a
    for num in range (1,ip_numbers + 1):
        password_numbers= random.choice(numbers)
        b= password_numbers
        easy_password += b
    for sym in range (1,ip_symbols + 1):
        password_symbols= random.choice(symbols)
        c= password_symbols
        easy_password += c
    print(easy_password)

# Hard password
hard_password = ""
if ip_difficulty == "Hard" or 2:
    hard_password == ''.join(random.sample(easy_password, len(easy_password)))
    print(hard_password)