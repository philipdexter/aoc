
with open('1.txt', 'r') as f:
  input = f.read().strip()


from dataclasses import dataclass, replace
@dataclass(unsafe_hash=True)
class poss:
  x: int
  y: int

pos1 = poss(0, 0)
pos2 = poss(0, 0)

delivered = {replace(pos1)}

import itertools
for santa, c in zip(itertools.cycle([pos1, pos2]), input):
  if c == '<':
    santa.x -= 1
  elif c == '>':
    santa.x += 1
  elif c == 'v':
    santa.y += 1
  elif c == '^':
    santa.y -= 1
  delivered.add(replace(santa))

print(len(delivered))
