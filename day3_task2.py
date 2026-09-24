# Pomodoro 2: analyze_scores(scores) — combining functions

# You've now got two working functions, get_grade(score) from yesterday and get_highest_lowest(scores) from just now. Time to make them work together.

# Write a new function called analyze_scores(scores) that:

# Takes a list of scores as input
# Calls your existing get_highest_lowest(scores) function internally to find the high and low
# Calls your existing get_grade(...) function internally, on both the highest and lowest scores, to get their letter grades
# Returns all four pieces: highest score, its grade, lowest score, its grade

# New idea here: a function can call other functions you already wrote, not just built-ins like len() or sum(). You don't need to rewrite the highest/lowest logic or the grade logic again, that work's already done, analyze_scores just needs to use them.

from day3_task1 import get_highest_lowest 
from day2_task2 import get_grade

test_scores = [95, 82, 71, 60, 45, 100, 79, 88]

def analyze_scores(scores):
  high, low = get_highest_lowest(scores)
  high_grade = get_grade(high)
  low_grade = get_grade(low)
  return high,low,high_grade,low_grade

print(analyze_scores(test_scores))