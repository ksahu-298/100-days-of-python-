# treasure Island game

print("Welcome to treasure island \n Your Mission Is To Find Treasure")

print("There are two roads left & right choose one")
opt_1= input("enter your choice L for Left & R for Right : ")
if opt_1 == 'R':
    print("Game Over")
else:
    print("You have come to a lake")
    print("There is an island in the middle of the lake")
    print("You can wait for a boat or swim across")
    opt_2 = input("enter your choice W for wait & S for swim : ")
    if opt_2 == 'S':
        print ("Game Over")
    else:
        print("You have arrived at the island unharmed")
        print("There is a house with 3 doors")
        print("One red, one yellow and one blue")
        opt_3 = input("Which colour do you choose R for Red , Y for Yellow & B for Blue ? : ")
        if opt_3 == 'R':
            print("Game Over")
        elif opt_3 == 'Y':
            print("You Win")
        elif opt_3 == 'B':
            print("Game Over")
        else:
            print("Game Over")

