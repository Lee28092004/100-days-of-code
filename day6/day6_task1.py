class Task:
  def __init__(self, description):
    self.description = description
    self.status = False

  def mark_done(self):
    self.status = True

  def is_done(self):
    return self.status

mytask = Task("Buy Milk")
mytask2 = Task("Walk dog")

mytask2.mark_done()
print(mytask.is_done())
print(mytask2.is_done())