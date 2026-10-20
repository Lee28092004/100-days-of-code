# Pomodoro 1: record the sales

# The cafe sells three items: Latte (RM 8.50), Toast (RM 5.00) and Cake (RM 7.00). Build a program that:

# Has a MenuItem class. Each item remembers its name, its price and how many it has sold, which starts at 0 and is not a parameter.
# Has a method on the class that records a sale of some quantity.
# Keeps the three items in a list.
# Loops: it shows the numbered menu, asks which item was sold and how many, and records it. Then it asks “Sell another? (yes / no)”.
# Rejects bad input. An item number that isn’t on the menu and a quantity below 1 should print a message and ask again.

# At the end, print how many of each item were sold.


class MenuItem:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.sold = 0

  def record_sale(self, sold):
    self.sold = self.sold + sold

menu = []

latte = MenuItem("Latte", 8.50)
toast = MenuItem("Toast", 5.00)
cake = MenuItem("Cake", 7.00)

answer = "yes"

menu.append(latte)
menu.append(toast)
menu.append(cake)

while answer.lower() == "yes":
  print("\n************************************")
  print("        Welcome to the Cafe         ")
  print("************************************")

  for number, item in enumerate(menu, start=1):
    print(number, item.name, item.price, item.sold)

  print("************************************")

  # Validate menu choice
  while True:
    try:
      choice = int(input("May I get your order? (1/2/3): "))

      if choice == 1 or choice == 2 or choice == 3:
        break
      else:
        print("Invalid answer. Please try again.")

    except ValueError:
      print("Invalid input. Please enter a whole number.")

  if choice == 1:
    while True:
      try:
        latte_choice = int(input("How many do you want?: "))

        if latte_choice >= 1:
          break
        else:
          print("Quantity must be at least 1.")

      except ValueError:
        print("Invalid input. Please enter a whole number.")

    menu[0].record_sale(latte_choice)
    answer = input("Sell another? (yes / no): ")

  elif choice == 2:
    while True:
      try:
        toast_choice = int(input("How many do you want?: "))

        if toast_choice >= 1:
          break
        else:
          print("Quantity must be at least 1.")

      except ValueError:
        print("Invalid input. Please enter a whole number.")

    menu[1].record_sale(toast_choice)
    answer = input("Sell another? (yes / no): ")

  elif choice == 3:
    while True:
      try:
        cake_choice = int(input("How many do you want?: "))

        if cake_choice >= 1:
          break
        else:
          print("Quantity must be at least 1.")

      except ValueError:
        print("Invalid input. Please enter a whole number.")

    menu[2].record_sale(cake_choice)
    answer = input("Sell another? (yes / no): ")

print("\n========== Final Sales Summary ==========")

for number, item in enumerate(menu, start=1):
  print(number, item.name, item.price, item.sold)
