
with open('1.txt') as f:
  input = f.readlines()

def proc(line):
  start, end = line.split(' => ')
  end = end.split(' ')
  pieces = [piece.split(' ') for piece in start.split(', ')]
  return pieces, end

input = [proc(line.strip()) for line in input]

recipes = {}
for start, end in input:
  recipes[end[1]] = (int(end[0]), [(b, int(a)) for a, b in start])

from collections import defaultdict
leftover = defaultdict(lambda: 0)

def to_get(what, want):
  if what == 'ORE':
    return want
  (gives, pieces) = recipes[what]
  if leftover[what] >= want:
    leftover[what] -= want
    return 0
  elif want <= gives:
    if want < gives:
      leftover[what] += gives - want
    return sum([to_get(*piece) for piece in pieces])
  else:
    return to_get(what, want - gives) + to_get(what, gives)

print(to_get('FUEL', 1))
