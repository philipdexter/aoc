
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
total = 0
for k in fabric:
  if len(fabric[k]) > 1:
    total += 1
print(total)
