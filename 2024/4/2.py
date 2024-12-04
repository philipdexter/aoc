
lines = []
for line in open('input.txt'):
  lines.append(line.strip())

def valid(x, y):
  return (0 <= x < len(lines)) and (0 <= y < len(lines[0]))

def get(x, y, dirx, diry):
  poss = [(x, y)]
  for _ in range(2):
    poss.append((poss[-1][0] + dirx, poss[-1][1] + diry))
  if any([not valid(x[0], x[1]) for x in poss]):
    return []
  return ''.join([lines[x][y] for x, y in poss])

def get_all(x, y):
  return [get(x, y, 1, 1), get(x, y+2, 1, -1)]

count = 0
for x in range(len(lines)):
  for y in range(len(lines[0])):
    a, b = get_all(x, y)
    if (a in ['MAS', 'SAM'] and b in ['MAS', 'SAM']):
      count += 1
print(count)
