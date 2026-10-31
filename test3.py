# 1 Project × 40 Marks

# Student Grade Book
# Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

# What you need to use
# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student




dict1 = {}

for i in range(0,4):
    name = input('enter name:')

    score = int(input('enter score:'))

    dict1[name] = score

    
print(dict1)
sum = 0
for i in dict1.values():
    sum = sum + i

print(sum)

average = sum//4
print(average)

print(max(dict1.values()))
print(min(dict1.values()))

dict1.get('amit')

