
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

lines = list(map(list, lines))

def at(x, y):
  return int(lines[x][y])

def right(x, y):
  return [at(x, y) for y in range(y+1, len(lines))]

def left(x, y):
  return [at(x, y) for y in range(y-1, -1, -1)]

def up(x, y):
  return [at(x, y) for x in range(x-1, -1, -1)]

def down(x, y):
  return [at(x, y) for x in range(x+1, len(lines))]

def sight(tree, seeing):
  l = 0
  for t in seeing:
    l += 1
    if t >= tree:
      break
  return l

def score_for(x, y):
  tree = at(x, y)
  l, r, u, d = left(x, y), right(x, y), up(x, y), down(x, y)
  return sight(tree, l) * sight(tree, r) * sight(tree, u) * sight(tree, d)

print(score_for(*max([(x, y) for x in range(len(lines)) for y in range(len(lines))], key=lambda x: score_for(*x))))
