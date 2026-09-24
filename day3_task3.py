# Pomodoro 3: Dictionaries, a new data type

# Quick primer before the task, since this is genuinely new syntax, not something to guess at.

# A list stores things in order, accessed by position: scores[0]. A dictionary stores things as key-value pairs, accessed by a name instead of a position:

# student = {"name": "Wallace", "score": 88}
# print(student["name"])   # prints Wallace
# print(student["score"])  # prints 88

# Each key ("name", "score") maps to a value. You can also loop through a dictionary's keys and values together:

# for key, value in student.items():
#     print(key, value)

# Your task: given this data,

# students = {"Alice": 92, "Ben": 55, "Chen": 78, "Dara": 40}

# Loop through it, and for each student, print their name, their score, and their letter grade, reusing your existing get_grade function.

from day2_task2 import get_grade

students = {"Alice": 92, "Ben": 55, "Chen": 78, "Dara": 40}

for name,score in students.items():
  print(name,score, get_grade(score))