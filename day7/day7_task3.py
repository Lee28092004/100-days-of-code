# Step 4 only: stop hard-coding the tasks and let the user add one.

# Ask the user for a description with input() and store it in a variable.
# Use that variable to create a new Task object.
# append it to tasks.
# Print len(tasks) to confirm the list grew.

# Put this before your loop, and remove the three hard-coded task1, task2 and task3 lines and their append lines, so the list starts empty.


class Task:
  def __init__(self, description):
    self.description = description
    self.status = False

  def mark_done(self):
    self.status = True

tasks = []

answer = "yes"

while answer == "yes":
  n = Task(input("Enter a task: "))
  tasks.append(n)
  answer = input("Add another (yes / no): ")

for task in tasks:
  print(task.description, task.status)

choice = int(input("Which task number is done?: "))

if choice <= 0:
  print("Invalid choice.")

elif choice > len(tasks):
  print("There no value in here")

else:
  tasks[choice-1].mark_done()

for task in tasks:
  print(task.description, task.status)

print(len(tasks))