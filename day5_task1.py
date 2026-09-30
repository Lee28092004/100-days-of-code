# Pomodoro 1: Core in-memory version, no file saving yet

# Build the basic mechanics first, before worrying about persistence. Write a program that:

# Keeps a list of tasks (just strings, task descriptions)
# Lets the user add a task
# Lets the user view all current tasks
# Lets the user remove a task
# Loops, asking the user what they want to do (add / view / remove / quit) until they choose to quit

def file_read():
    with open("task.txt", "r") as file:
      current_task = file.read()
    print("\n",current_task, "\n")
    return(current_task)

number = 0

while True:
  print("--------------------------------------------")
  print("Adminstrator Choices")
  print("1. Add a task")
  print("2. View all current task")
  print("3. Remove a task")
  print("--------------------------------------------")

  choice = int(input("Enter a option (1/2/3): "))

  if choice == 1:
    add_task = input("Please enter a task you want here: ")
    number += 1
    with open("task.txt", "a") as file:
      file.write(f"{number} : {add_task}\n")
    print("Added a new task.\n")

  elif choice == 2:
    file_read()
    print("File read complete.\n")

  elif choice == 3:
    lines = file_read().splitlines()
    remove_task = int(input("Select which task you want to remove by using (1/2/3/4...): "))

    with open("task.txt", "w") as file:
      for line in lines:
        if int(line.split(":")[0]) != remove_task:
          file.write(line + "\n")

    print("Line remove complete.\n")

  else:
    print("Invalid option. Please Try Again.")
    