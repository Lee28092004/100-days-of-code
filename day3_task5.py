# Pomodoro 5: Bringing it all together

# Last one for today, so let's combine everything you've built across all three days into one task, dictionaries, error handling, and your existing functions.

# student_scores = {"Alice": 92, "Ben": "eighty", "Chen": 78, "Dara": 40, "Eli": 105}

# Notice two problems planted in this data on purpose: "Ben" has a score typed as text instead of a number, and "Eli" has 105, which is above 100, not a realistic score.

# Your task: write a function called process_students(students) that:

# Loops through the dictionary
# For each student, safely gets their grade using safe_grade (handles Ben's text problem automatically, you already built this)
# Separately checks if the score is above 100, and if so, treat it as invalid too, print something like "Eli: Invalid score (out of range)" instead of trying to grade it
# For everyone else, print name, score, and grade normally

student_scores = {"Alice": 92, "Ben": "eighty", "Chen": 78, "Dara": 40, "Eli": 105}

from day3_task4 import safe_grade
from day2_task2 import get_grade

def process_students(students):
  for name, score in students.items():
    if not isinstance(score, int):
      print(score,": Is not a real number")

    elif score > 100:
      print(name,": Invalid score (out of range)")

    else:
      print(safe_grade(score))

process_students(student_scores)