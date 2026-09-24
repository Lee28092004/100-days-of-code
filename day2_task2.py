# Extend get_grade slightly

# You've got a working function that takes one score and returns a letter. Now think through this conceptually first, before touching code:

# You've got your list, test_scores = [95, 82, 71, 60, 45, 100, 79, 88]. Right now get_grade only handles one score at a time. Write a loop that goes through every score in test_scores, calls get_grade on each one, and prints the result for all 8.

test_scores = [95, 82, 71, 60, 45, 100, 79, 88]

def get_grade(score):
  if score < 60:
    return "F"

  elif 60 <= score <= 69:
    return "D"

  elif 70 <= score <= 79:
    return "C"

  elif 80 <= score <= 89:
    return "B"

  else:
    return "A"

# for score in test_scores:
#   print(get_grade((score)))