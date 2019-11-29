
with open('1.txt', 'r') as f:
  input = f.read().strip()


from dataclasses import dataclass, asdict
@dataclass(unsafe_hash=True)
class poss:
  x: int
  y: int

pos = poss(0, 0)

delivered = {pos}

for c in input:
  if c == '<':
    pos.x -= 1
  elif c == '>':
    pos.x += 1
  elif c == 'v':
    pos.y += 1
  elif c == '^':
    pos.y -= 1
  delivered.add(poss(**asdict(pos)))

print(delivered)
print(len(delivered))
