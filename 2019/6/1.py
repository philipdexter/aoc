
with open('1.txt') as f:
  input = f.readlines()

map = {}

for line in input:
  line = line.strip()
  if not line: continue
  orbitee, orbiter = line.split(')')
  map[orbiter] = orbitee

def depth(p):
  if p == 'COM':
    return 0
  return 1 + depth(map[p])

agg = 0
for p in map.keys():
  agg += depth(p)
print(agg)
