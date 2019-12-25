
input = [
  [False, False, True, False, True, ],
  [False, True, False, True, True, ],
  [True, True, False, False, False, ],
  [False, True, False, True, False, ],
  [True, True, True, False, False, ],]

# input = [
#   [False, False, False, False, True, ],
#   [True, False, False, True, False, ],
#   [True, False, False, True, True, ],
#   [False, False, True, False, False, ],
#   [True, False, False, False, False, ],
# ]

state = input

def pr():
  for y in range(len(state)):
    for x in range(len(state[0])):
      if state[y][x]:
        print('#', end='')
      else:
        print('.', end='')
    print()

def adj(x, y):
  return [state[y1][x1]
          for (x1, y1) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
          if 0 <= x1 < len(state[0])
          if 0 <= y1 < len(state)]

def next(x, y):
  if state[y][x]:
    return True if sum(adj(x, y)) in [1] else False
  else:
    return True if sum(adj(x, y)) in [1, 2] else False

def step():
  global state
  new_state = [[next(x, y) for x in range(len(state[0]))] for y in range(len(state))]
  state = new_state

def hs():
  return str(state)

def bdr():
  agg = 0
  p = 0
  for y in range(len(state)):
    for x in range(len(state[0])):
      p += 1
      if state[y][x]:
        agg += 2 ** (p - 1)
  return agg


prev = set()
while True:
  step()
  h = hs()
  if h in prev:
    pr()
    break
  prev.add(h)
print(bdr())
