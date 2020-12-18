import re

class F:
  def __init__(self, n):
    self.n = n

  def __add__(self, other):
    return F(self.n + other.n)
  def __and__(self, other):
    return F(self.n * other.n)

input = []
for line in open('1.txt'):
  input.append(re.sub(r'\*', '&', re.sub(r'(\d+)', r'F(\1)', line.strip())))

agg = 0
for line in input:
  agg += eval(line).n
print(agg)
