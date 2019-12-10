
with open('1.txt') as f:
  input = f.readlines()

# input = ['.#..#',
#          '.....',
#          '#####',
#          '....#',
#          '...##',]

# input = ['......#.#.',
#          '#..#.#....',
#          '..#######.',
#          '.#.#.###..',
#          '.#..#.....',
#          '..#....#.#',
#          '#..#....#.',
#          '.##.#..###',
#          '##...#..#.',
#          '.#....####',
#          ]

# input = ['#.#...#.#.',
#          '.###....#.',
#          '.#....#...',
#          '##.#.#.#.#',
#          '....#.#.#.',
#          '.##..###.#',
#          '..#...##..',
#          '..##....##',
#          '......#...',
#          '.####.###.',]

# input = ['.#..##.###...#######',
#          '.##.############..##.',
#          '.#.######.########.#',
#          '.###.#######.####.#.',
#          '#####.##.#.##.###.##',
#          '..#####..#.#########',
#          '####################',
#          '#.####....###.#.#.##',
#          '##.#################',
#          '#####.##.###..####..',
#          '..######..##.#######',
#          '####.##.####...##..#',
#          '.#####..#.######.###',
#          '##...#.##########...',
#          '#.##########.#######',
#          '.####.#.###.###.#.##',
#          '....##.##.###..#####',
#          '.#.#.###########.###',
#          '#.#.#.#####.####.###',
#          '###.##.####.##.#..##']

asteroids = []
for y in range(len(input)):
  for x in range(len(input[y])):
    if input[y][x] == '#':
      asteroids.append((x, y))


def diff(f, t):
  if f[0] == t[0]:
    return (0, 1 if t[1] > f[1] else -1)
  elif f[1] == t[1]:
    return (1 if t[0] > f[0] else -1, 0)
  x = t[0] - f[0]
  y = t[1] - f[1]
  import math
  l = math.gcd(x, y)
  return (x // l, y // l)
def out(p):
  if p[0] < 0 or p[1] < 0: return True
  if p[0] >= len(input[0]) or p[1] >= len(input): return True
  return False
def diff_points(f, d):
  res = []
  f = (f[0] + d[0], f[1] + d[1])
  while not out(f):
    res.append(f)
    f = (f[0] + d[0], f[1] + d[1])
  return res

loss = []
for f in asteroids:
  can_see = asteroids[:]
  can_see.remove(f)
  while True:
    for a in can_see:
      dp = diff_points(a, diff(f, a))
      removed = False
      for p in dp:
        if p in can_see:
          can_see.remove(p)
          removed = True
      if removed:
        break
    else:
      break
  loss.append((f, len(can_see)))
  print(f'{f} {len(can_see)} {can_see}')
print(max(loss, key=lambda x: x[1]))
