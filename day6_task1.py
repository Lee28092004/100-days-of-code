class Task:
  def __init__(self, description):
    self.description = description
    self.status = False

  def mark_done(self):
    self.status = True

mytask = Task("Buy Milk")
mytask2 = Task("Walk dog")

print(mytask2.status)
mytask2.mark_done()
print(mytask2.status)
print(mytask.status)