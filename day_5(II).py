# Fizzbuzz game
print ("Welcome to the FizzBuzz game")
for integer in range(1,101):
    if integer % 3 == 0:
        print("FIZZ")
    elif integer % 5 == 0:
        print("BUZZ")
    elif integer % 3 == 0 and integer % 5 == 0:
        print("FIZZBUZZ")
    else:
        print(integer)