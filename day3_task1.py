# Pomodoro 1: get_highest_lowest(scores)

# Remember Pomodoro 5 from Day 1, the highest/lowest logic where you first copied from Google, then didn't quite finish untangling it yourself? Let's close that loop properly.

# Write a function called get_highest_lowest(scores) that:

# Takes a list of scores as input
# Finds the highest and lowest without using max() or min()
# Returns both values

# New idea you haven't used yet: a function can return more than one value at once, separated by a comma, like return a, b. When you call it, you can catch both on the other side like high, low = get_highest_lowest(test_scores).


test_scores = [95, 82, 71, 60, 45, 100, 79, 88]

def get_highest_lowest(scores):
  high, low = test_scores[0], test_scores[0]

  for scores in test_scores:
    if scores > high:
        high = scores
    
    if scores < low:
        low = scores

  return high,low

print(get_highest_lowest(test_scores))