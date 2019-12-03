
with open('1.txt') as f:
  input = f.readlines()

w1 = input[0].strip()
w2 = input[1].strip()

def add(a, b):
  x, y = a
  c, d = b
  return (x + c, y + d)

def parsewire(wire):
  pos = (0, 0)
  poss = set()
  for piece in wire.split(','):
    direction, distance = piece[0:1], int(piece[1:])
    if direction == 'L':
      mod = (-1, 0)
    elif direction == 'R':
      mod = (1, 0)
    elif direction == 'U':
      mod = (0, 1)
    elif direction == 'D':
      mod = (0, -1)
    else:
      raise Exception('failed direction: ' + direction)
    for i in range(distance):
      pos = add(pos, mod)
      poss.add(pos)
  return poss

poss1 = parsewire(w1)
poss2 = parsewire(w2)
closest = min(poss1.intersection(poss2), key=lambda x: abs(x[0]) + abs(x[1]))
print(closest)
print(sum(closest))
