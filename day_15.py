# COFFEE MACHINE PROGRAM

menu = {
    "espresso": { 
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
            "cost": 1.5,
        },
    },
    "latte": { 
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
            "cost": 2.5,
        },
    },
    "cappuccino": { 
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
            "cost": 3.0,
        },
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_resources():                    
    '''Prints the remaining resources in the coffee machine.'''                                                            
    for item in resources:
        print(f"{item}: {resources[item]}ml")

user_choice = input("Would you like to use the coffee machine? (yes/no)".lower())
if user_choice == "no":
    print("Goodbye!")
    order = "no"
elif user_choice == "yes":
    order = "yes"
else:
    print("Invalid input. Please try again.")
    order = "no"    

while order == "yes":
    print("Welcome to the coffee machine!")
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(f"You have selected {user_input}.")

    print("Your remaining resources are: " )
    print_resources()

    def check_resources(order_ingredients):
        '''Checks if there are enough resources to make the selected drink.'''
        if user_input == "espresso":
            print("Espresso is being made.")
            return order_ingredients["water"] <= resources["water"] and order_ingredients["coffee"] <= resources["coffee"]
        
        elif user_input == "latte":
            print("Latte is being made.")
            return order_ingredients["water"] <= resources["water"] and order_ingredients["coffee"] <= resources["coffee"] and order_ingredients["milk"] <= resources["milk"]
            
        elif user_input == "cappuccino":
            print("Cappuccino is being made.")
            return order_ingredients["water"] <= resources["water"] and order_ingredients["coffee"] <= resources["coffee"] and order_ingredients["milk"] <= resources["milk"]
            
        else:
            print("There are not enough resources to make this drink at the moment. Please come back later or try another drink. 😱")
            return False
        
    check_resources(menu[user_input]["ingredients"])

    def process_coins():
        '''Calculates the total amount of money inserted by the user.'''
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickles = int(input("How many nickles? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total

    if user_input == "espresso":
        total = process_coins()
        if total >= menu[user_input]["ingredients"]["cost"]:
            change = round(total - menu[user_input]["ingredients"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso. Enjoy! 🍵")
            resources["water"] -= menu[user_input]["ingredients"]["water"]
            resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]
        else:
            print("Sorry, that's not enough money. Money refunded.")

    elif user_input == "latte":
        total = process_coins()
        if total >= menu[user_input]["ingredients"]["cost"]:
            change = round(total - menu[user_input]["ingredients"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your latte. Enjoy! 🍵")
            resources["water"] -= menu[user_input]["ingredients"]["water"]
            resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]
            resources["milk"] -= menu[user_input]["ingredients"]["milk"]
        else:
            print("Sorry, that's not enough money. Money refunded.")

    elif user_input == "cappuccino":
        total = process_coins()
        if total >= menu[user_input]["ingredients"]["cost"]:
            change = round(total - menu[user_input]["ingredients"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino. Enjoy! 🍵")
            resources["water"] -= menu[user_input]["ingredients"]["water"]
            resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]
            resources["milk"] -= menu[user_input]["ingredients"]["milk"]
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid input. Please try again.")
    
    print("remaining resources is ",)
    print_resources()