# Pomodoro 4: Basic error handling

# New concept, quick primer:

# Right now, if your get_grade function got passed something that isn't a number, like text, it would crash the whole program. try and except let you catch that crash and handle it gracefully instead:

# try:
#     risky_code_that_might_fail()
# except:
#     print("Something went wrong")

# Python attempts the code inside try. If it hits an error, instead of crashing, it jumps to except and runs that instead.

# Your task: write a function called safe_grade(score) that:

# Tries to call get_grade(score) and return its result
# If score isn't actually a number (someone passes in text by mistake), catch that error instead of crashing, and return "Invalid score" instead

from day2_task2 import get_grade

def safe_grade(score):
  try:
    return get_grade(score)

  except:
    return("Invalid score")


# print(safe_grade("Ninety"))