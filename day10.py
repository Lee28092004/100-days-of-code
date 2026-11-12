# Number Guessing Game in Python
# Last Updated :
# Number Guessing Game is a game in which the computer randomly selects a number between 1 and 100. The user must guess the number within a limited number of attempts. After each incorrect guess, the program provides a hint indicating whether the guess is too low or too high.

# In this game, randint() is used to generate a random number within the specified range.

# Winning Rules
# Computer generates a random number between 1 and 100.
# User has a maximum of 7 attempts to guess the number.
# User wins immediately if the guess matches the randomly generated number.
# If the guess is lower than the selected number, the program displays "Too Low" and the user should try a higher number.
# If the guess is higher than the selected number, the program displays "Too High" and the user should try a lower number.
# Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.
# If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.

import random

computer = random.randint(1, 100)
user_attempt = 1
won = False

def rules():
  print("\nWelcome to Number Guessing Game!\n")
  print("I have selected a number between 1 and 100.\n")
  print("You have 7 attempts to guess it.")


rules()


while user_attempt < 8 and not won:
  try:
    user_answer = int(input(f"Attempt {user_attempt}/7 - What are you guessing for the number: "))

    if user_answer < 1 or user_answer > 100:
      print("Please stay within 1 to 100.\n")
      continue

    if user_answer == computer:
      print(f"\nCongratulations. You WIN! The answer is: {computer}\n")
      won = True

    elif user_answer < computer:
      print("\nToo Low. Try a higher number.\n")
      user_attempt += 1

    elif user_answer > computer:
      print("\nToo High. Try a lower number.\n")
      user_attempt += 1

    else:
      print("Invalid Input. Please Try Again.\n")
      
  except ValueError:
    print("Please enter a valid number.\n")

if won == False:
  print(f"\nYou lose. The answer is: {computer}\n")