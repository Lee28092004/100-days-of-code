# Build a to-do list program that saves to a file.
# The user can add a task, view all tasks, mark a task as done, and quit. The tasks and their done status must still be there the next time the program runs.

def rules():
  print("\nWelcome to the TO-DO List.")
  print("1. Add a Task.")
  print("2. View all Task")
  print("3. Mark a task as Done")
  print("4. Exit\n")

choice = 0

while choice != 4:
  try:
    rules()
    choice = int(input("Please choose anything you wanted to do: "))
    if choice == 1:
      user_task = input("What do you wanna add in a Task: ")
      with open("todo.txt", "a") as file:
        file.write(f"{user_task} \n")
        print("File Append Successful.\n")

    elif choice == 2:
      try:
        with open("todo.txt", "r") as file:
          lines = file.read().splitlines()          # blank 1: same method as option 3, with brackets

        print("Here the current list.\n")
        for position, line in enumerate(lines, start=1):     # blank 2: your loop variable name from option 3
          print(position, line)                              # blank 3: same name as blank 2

      except FileNotFoundError:
        print("File does not Exist. Please Add a Task.\n")

    elif choice == 3:
      try:
        with open("todo.txt", "r") as file:
          lines = file.read().splitlines()          # blank 1: split text into lines (with brackets)

        for position, line in enumerate(lines, start=1):
          print(position, line)

        task_done = int(input("Which task do you wanna mark as DONE?: "))

        if task_done >= 1 and task_done <= len(lines):      # blank 2: how many lines exist
          lines[task_done - 1] = lines[task_done - 1] + " (Done)"
          with open("todo.txt", "w") as file:
            file.write("\n".join(lines) + "\n")
          print("Task Successfully mark as Done")

        else:
          print("Invalid task number.")

      except FileNotFoundError:
        print("File does not Exist. Please Add a Task.\n")
      
    elif choice == 4:
      print("Thank you for your time.\n")
      break

    else:
      print("Please choose the number within the TO-DO List Menu.\n")

  except ValueError:
    print("Invalid Input. Please Try Again")  