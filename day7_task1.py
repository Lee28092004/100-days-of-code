# Pomodoro 1 (25 min): open a new file and write the Task class from scratch, without looking at the one above. It needs:
# description stored from a parameter
# a status that starts as False with no parameter
# a mark_done method that sets the status to True
# an is_done method that returns the status

class Task:
  def __init__(self, description):
    self.description = description
    self.status = False
    self.priority = "low"

  def mark_done(self):
    self.status = True

  def is_done(self):
    return self.status

  def set_priority(self, priority):
    self.priority = priority


task1 = Task("Buy Milk")
task2 = Task("Walk dog")

task1.set_priority("high")

print(task1.priority)
print(task2.priority)