# Pomodoro 3: Keep calculating until the user quits

# Task: wrap your get_calculator_input() call in a loop so the calculator keeps asking for new calculations repeatedly. After each calculation, ask the person if they want to do another one, something like "Calculate again? (yes/no)". If they type anything other than "yes", the loop should stop and the program ends.

from day4_task2 import get_calculator_input

answer = "yes"


while answer == "yes":
  print(get_calculator_input())
  answer= input("Calculate again? (yes/no): ")

  while answer != "yes" and answer != "no":
    answer = input("Invalid answer. Please try Again (yes/no): ")