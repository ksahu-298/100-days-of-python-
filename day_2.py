#Project - TIP CALCULATOR

print("Welcome to the tip calculator")
bill = float(input("What was your total bill ? "))
tip = int(input("How much tip percentage you want to give ? 10 , 12 or 15" ))
split = int(input("In how many people you want to split your bill ?" ))

tip_per = tip/100
 
total_bill = (bill*tip_per) + bill

bill_per_per= total_bill/split
amount = round(bill_per_per,2)

print(f"Your bill was of {bill} INR & you want to give tip {tip} INR & you want to split the bill in {split} people")
print(f"Your total bill is {total_bill} INR & Each person should pay {amount} INR")
