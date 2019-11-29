
with open('1.txt', 'r') as f:
  input = f.read()

floor = 0

for i, c in enumerate(input.strip()):
  if c == '(':
    floor += 1
  elif c == ')':
    floor += -1
  if floor < 0:
    print(i+1)
    exit(0)


print(floor)
