# Pomodoro 3: Grade classifier
# Loop through this list of test scores: 95, 82, 71, 60, 45, 100, 79, 88
# For each score, print a grade:
# 90 or above: "A"
# 80 to 89: "B"
# 70 to 79: "C"
# 60 to 69: "D"
# Below 60: "F"

test_scores = [95, 82, 71, 60, 45, 100, 79, 88]

for item in test_scores:
  if item < 60:
    print("F")

  elif 60 <= item <= 69:
    print("D")

  elif 70 <= item <= 79:
    print("C")

  elif 80 <= item <= 89:
    print("B")

  else:
    print("A")