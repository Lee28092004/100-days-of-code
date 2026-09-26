# Day 4, and this is a good one, time to build your first actual project instead of isolated exercises: a command-line calculator.

# This pulls together everything you've built across Days 1 to 3, functions, conditionals, error handling, and adds one new piece, input() to actually take numbers from a person typing, not a hardcoded list.

# The mission for today, broken into stages across multiple Pomodoros:

# Pomodoro 1: Basic version, no error handling yet
# Write a function calculate(num1, operator, num2) that:

# Takes two numbers and an operator symbol (+, -, *, /) as input
# Returns the correct result based on which operator was passed in
# Test it by calling it directly a few times, like print(calculate(10, "+", 5)), print(calculate(10, "/", 0))

# Think about the structure before coding: you're checking which one of four possible operators was passed in, that's a multi-branch decision, same shape you've used repeatedly this week, just comparing against "+", "-", "*", "/" instead of numbers this time.

def calculate(num1, operator, num2):
  if operator == "+":
    ans = num1 + num2

  elif operator == "-":
    ans = num1 - num2

  elif operator == "*":
    ans = num1 * num2

  elif operator == "/":
    if num2 == 0:
      ans = "Not able to calculate since could not divide by 0."
    else:
      ans = num1 / num2

  else:
    ans = "Invalid answer. Please try again"

  return(ans)

# print(calculate(10, "/", 5))
# print(calculate(10, "/", 0))
# print(calculate(0, "/", 5))
# print(calculate(10, "%", 5))