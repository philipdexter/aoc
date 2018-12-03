
def parse(s):
  parts = s.rstrip().split()
  [x, y] = list(map(int, parts[2].rstrip(':').split(',')))
  [width, height] = list(map(int, parts[3].split('x')))
  return (parts[0], x, y, width, height)


fabric = {}
with open('1') as f:
  for line in f:
    id, x, y, width, height = parse(line)
    for i in range(x, x+width):
      for j in range(y, y+height):
        if not fabric.get((i,j)):
          fabric[(i,j)] = set()
        fabric[(i,j)].add(id)
not_overlap = set()
overlap = set()
for k in fabric:
  ids = fabric[k]
  if len(ids) == 1:
    [id] = list(ids)
    if id not in overlap:
      not_overlap.add(id)
  else:
    for id in ids:
      overlap.add(id)
      if id in not_overlap:
        not_overlap.remove(id)
print(not_overlap)
