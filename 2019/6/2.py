
with open('1.txt') as f:
  input = f.readlines()

map = {}

for line in input:
  line = line.strip()
  if not line: continue
  orbitee, orbiter = line.split(')')
  map[orbiter] = orbitee

def path(p):
  if p == 'COM':
    return []
  return [p] + path(map[p])

you_path = path('YOU')
san_path = path('SAN')

for p in you_path:
  try:
    san_path.index(p)
    print(p)
    print(you_path.index(p))
    print(san_path.index(p))
    print(you_path.index(p) - 1 + san_path.index(p) - 1)
    break
  except ValueError:
    continue
