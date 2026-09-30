# Pomodoro 4: Grade classifier v2, with stats
# Using the same list as before, test_scores = [95, 82, 71, 60, 45, 100, 79, 88], extend what you already built:
# Keep classifying and printing each grade like before
# Also count how many A's, B's, C's, D's, and F's there are in total
# After the loop finishes, print those five counts
# Also calculate and print the average of all the scores

test_scores = [95, 82, 71, 60, 45, 100, 79, 88]
a,b,c,d,f = 0,0,0,0,0
total = sum(test_scores)

for item in test_scores:
  if item < 60:
    print("F")
    f += 1

  elif 60 <= item <= 69:
    print("D")
    d += 1

  elif 70 <= item <= 79:
    print("C")
    c += 1

  elif 80 <= item <= 89:
    print("B")
    b += 1

  else:
    print("A")
    a += 1

print("Total A = " + str(a))
print("Total B = " + str(b))
print("Total C = " + str(c))
print("Total D = " + str(d))
print("Total F = " + str(f))
print("The total average score is: " + str(int(total/len(test_scores))))