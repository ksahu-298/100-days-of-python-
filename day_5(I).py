#repliacte max funtion of list using for loop
students_score = [102,103,899,564,93,8004,299,1000,1001]
print(max(students_score))                      # max function is used to find the maximum value in a list
max_score=0

for maximum_score in students_score:
    if maximum_score > max_score:
        max_score = maximum_score

print(max_score)

