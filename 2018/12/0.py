
state = [0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
zero = 3

rules = [
 [[0,0,0,1,1], 1],
 [[0,0,1,0,0], 1],
 [[0,1,0,0,0], 1],
 [[0,1,0,1,0], 1],
 [[0,1,0,1,1], 1],
 [[0,1,1,0,0], 1],
 [[0,1,1,1,1], 1],
 [[1,0,1,0,1], 1],
 [[1,0,1,1,1], 1],
 [[1,1,0,1,0], 1],
 [[1,1,0,1,1], 1],
 [[1,1,1,0,0], 1],
 [[1,1,1,0,1], 1],
 [[1,1,1,1,0], 1],
 ]

def match(x):
  for rule in rules:
    if x == rule[0]:
      return rule[1]
  return 0

generation = 0

def step():
  global state
  next_generation = []
  for i in range(len(state)):
    if i > 1 and i < len(state)-2:
      n = match(state[i-2:i+3])
    else:
      n = 0
    next_generation.append(n)
  state = next_generation

def convert(s):
  for s in state:
    if s == 0:
      print('.', end='')
    else:
      print('#', end='')
  print()

convert(state)
for i in range(20):
  step()
  convert(state)
agg = 0
for i, x in enumerate(state):
  if x == 1:
    print(i-zero)
    agg += i-zero
print(agg)
