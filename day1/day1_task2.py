# Loop through numbers 1 to 50. For each number:

# If it's divisible by both 4 and 6, print "Quad"
# Else if it's divisible by 4, print "Four"
# Else if it's divisible by 6, print "Six"
# Else if it's negative (won't happen here, but structure for it anyway), print "Negative"
# Otherwise, print the number

num = 0
while num < 50:
  num += 1
  if num < 0:
    print("Negative")

  elif num % 4 == 0 and num % 6 == 0:
    print("Quad")

  elif num % 4 == 0:
    print("Four")

  elif num % 6 == 0:
    print("Six")

  else:
    print(num)