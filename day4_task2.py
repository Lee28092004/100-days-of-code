# Pomodoro 2: Real input, with error handling

# Now let's make this actually usable by a person typing, not just hardcoded test calls, and protect it from bad input the way you did with safe_grade yesterday.

# Two new failure points to think about, compared to yesterday:

# Someone types a number wrong, like letters instead of digits, when entering num1 or num2. Remember what int(input(...)) does if the text can't be converted to a number, think back to what you tested with isinstance yesterday, a similar kind of failure.
# Someone types an operator that isn't one of your four, like % or x. Your function already has an else branch catching this at the calculation stage, but that's only useful if the bad input even reaches that point without crashing earlier.

# Your task: write a new function, get_calculator_input(), that:

# Uses input() to ask the person for num1, an operator, and num2, same three prompts as your very first attempt today
# Wraps the number conversions in try/except, so if someone types something that can't convert to a number, it doesn't crash, instead print something like "That's not a valid number" and don't proceed to calculate
# If the numbers are valid, call your existing calculate(num1, operator, num2) function and print the result

from day4_task1 import calculate


def get_calculator_input():
  try:
    num1 = int(input("Enter a number for num1: "))
    num2 = int(input("Enter a number for num2: "))
    operator = input("Enter an operator you wanted to calculate num1 & num2 (+, -, *, /): ")  
    result = calculate(num1, operator, num2)
    return isinstance(result, (int, float))

  except:
    return("That's not a valid number.")


print(get_calculator_input())