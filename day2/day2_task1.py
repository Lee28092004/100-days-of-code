# Write get_grade(score)

# Take the classification logic you already built and proved you understand, correctly, twice, tonight, and wrap it inside a function instead of a loop.

# Shape to follow:

# def get_grade(score):
#     if ...
#         return ...
#     elif ...
#         return ...
#     ...

# Key difference from before: instead of print()ing the grade inside the loop, you're using return to hand the letter grade back out of the function. Same boundary logic as your grade classifier, same ordering rules, just swap print for return.

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

print(get_grade(88))