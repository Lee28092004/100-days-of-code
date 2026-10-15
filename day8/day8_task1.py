class Task:
  def __init__(self, description):
    self.description = description
    self.status = False

  def mark_done(self):
    self.status = True


def task_description():
  for task in tasks:
    print(task.description, task.status)

tasks = []

answer = "yes"
second_answer = "yes"

while answer == "yes":
  descriptions = (input("Enter a task: "))
  if len(descriptions.strip()) > 0:
    n = Task(descriptions)
    tasks.append(n)
    answer = input("Add another (yes / no): ")
    while answer != "yes" and answer != "no":
        answer = input("Invalid Input. Please Try again. Add another (yes / no): ")

  else:
    print("Wrong answer. Please Try Again\n")

task_description()

while second_answer == "yes":
  choice = int(input("Which task number is done?: "))
  if choice <= 0:
    print("Invalid choice.\n")

  elif choice > len(tasks):
    print("There no value in here.\n")

  else:
    tasks[choice-1].mark_done()
    task_description()
    second_answer= input("Change another (yes / no): ")
    while second_answer != "yes" and second_answer != "no":
        second_answer = input("Invalid Input. Please Try again. Change another (yes / no): ")

task_description()
print(len(tasks))