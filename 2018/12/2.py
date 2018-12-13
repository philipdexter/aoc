
state = [0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1]
zero = 1

rules = {
  (0,0,1,0,0) : 0,
  (0,0,1,0,1) : 0,
  (1,0,1,0,0) : 0,
  (0,1,0,0,1) : 0,
  (1,0,0,0,0) : 0,
  (0,0,0,0,1) : 0,
  (0,1,0,1,0) : 1,
  (1,0,1,1,1) : 0,
  (1,1,1,1,0) : 0,
  (0,0,0,0,0) : 0,
  (0,1,0,0,0) : 1,
  (1,1,1,1,1) : 1,
  (0,1,1,1,1) : 0,
  (1,0,0,1,0) : 1,
  (1,0,0,0,1) : 1,
  (0,1,1,1,0) : 0,
  (1,1,1,0,1) : 1,
  (0,0,0,1,1) : 1,
  (1,0,1,1,0) : 1,
  (0,1,0,1,1) : 1,
  (1,1,0,1,0) : 1,
  (0,0,0,1,0) : 0,
  (0,0,1,1,1) : 1,
  (1,1,1,0,0) : 1,
  (1,1,0,0,0) : 0,
  (0,0,1,1,0) : 0,
  (0,1,1,0,1) : 0,
  (1,1,0,1,1) : 0,
  (0,1,1,0,0) : 0,
  (1,1,0,0,1) : 1,
  (1,0,1,0,1) : 0,
  (1,0,0,1,1) : 1,
  }

def match(x):
  return rules.get(tuple(x), 0)

generation = 0

cache = {}

def expand():
  global state
  global zero
  if 1 in state[-5:]:
    state += [0,0,0,0,0]
  if 1 in state[:5]:
    state = [0,0,0,0,0] + state
    zero += 5

def step():
  global state
  global cache
  next_generation = []
  if len(cache) > 100000:
    cache = {}
  for i in range(len(state)):
    if i > 1 and i < len(state)-2:
      # if cache.get(tuple(state[i-2:])):
      #   next_generation += cache[tuple(state[i:])]
      #   break
      n = match(state[i-2:i+3])
    else:
      n = 0
    next_generation.append(n)
    cache[tuple(state[:i])] = next_generation[:]
  state = next_generation

def convert(s):
  for s in state:
    if s == 0:
      print('.', end='')
    else:
      print('#', end='')
  print()

def answer():
  agg = 0
  for i, x in enumerate(state):
    if x == 1:
      agg += i-zero
  print(agg)

convert(state)
for i in range(50000000000):
  expand()
  step()
  print('=====')
  print(i)
  print(len(state))
  answer()
  # convert(state)

answer()
