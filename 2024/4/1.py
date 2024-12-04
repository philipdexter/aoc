
lines = []
for line in open('input.txt'):
  lines.append(line.strip())

def valid(x, y):
  return (0 <= x < len(lines)) and (0 <= y < len(lines[0]))

def get(x, y, dirx, diry):
  poss = [(x, y)]
  for _ in range(3):
    poss.append((poss[-1][0] + dirx, poss[-1][1] + diry))
  if any([not valid(x[0], x[1]) for x in poss]):
    return []
  return ''.join([lines[x][y] for x, y in poss])

def get_all(x, y):
  return [x for x in [get(x, y, -1, -1),
                      get(x, y, -1, 0),
                      get(x, y, -1, 1),
                      get(x, y, 0, -1),
                      get(x, y, 0, 1),
                      get(x, y, 1, -1),
                      get(x, y, 1, 0),
                      get(x, y, 1, 1)]
          if x]

count = 0
for x in range(len(lines)):
  for y in range(len(lines[0])):
    for s in get_all(x, y):
      if s == 'XMAS':
        count += 1
print(count)
