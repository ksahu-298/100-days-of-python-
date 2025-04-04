# who's going to pay bill using list datatype   
import random
print("Who's going to pay the bill?")
print("Enter the bill amount :")
a = int(input())

friends= ["karan", "Kushagra", "Shanaya" , "Vaishnavi", "vivek"]
bill = random.choice(friends)
print("The person who is going to pay the bill is : " + bill)