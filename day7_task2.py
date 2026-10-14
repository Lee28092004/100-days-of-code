# Next is Pomodoro 2, where the class goes into a real program. Your day 5 app stored tasks as lines of text in a file, and now it will hold Task objects in a list.

# First step only:

# Create an empty list called tasks.
# Add three Task objects to it, with descriptions of your choice.
# Mark one of them done.
# Use a for loop to print each task’s description and whether it is done.

class Task:
  def __init__(self, description):
    self.description = description
    self.status = False

  def mark_done(self):
    self.status = True

task1 = Task("Buy Milk")
task2 = Task("Walk Dog")
task3 = Task("Run")

tasks = []
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

print(len(tasks))
task2.mark_done()

for task in tasks:
  print(task.description, task.status)