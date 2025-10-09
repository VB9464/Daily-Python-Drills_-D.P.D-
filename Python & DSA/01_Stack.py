class stack:
  def __init__(self):
    self.values = []
  def push(self,x):
    self.values = [x]+self.values

  def pop(self):
    return self.values.pop(0)

s = stack()
s.push(10)
s.push(20)
print(s.values)
