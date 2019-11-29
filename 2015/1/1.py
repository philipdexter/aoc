
with open('1.txt', 'r') as f:
  input = f.read()

floor = 0

for c in input.strip():
  if c == '(':
    floor += 1
  elif c == ')':
    floor += -1


print(floor)
