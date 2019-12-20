
with open('1.txt') as f:
  input = f.readlines()

# input = [
#   '         A',
#   '         A',
#   '  #######.#########',
#   '  #######.........#',
#   '  #######.#######.#',
#   '  #######.#######.#',
#   '  #######.#######.#',
#   '  #####  B    ###.#',
#   'BC...##  C    ###.#',
#   '  ##.##       ###.#',
#   '  ##...DE  F  ###.#',
#   '  #####    G  ###.#',
#   '  #########.#####.#',
#   'DE..#######...###.#',
#   '  #.#########.###.#',
#   'FG..#########.....#',
#   '  ###########.#####',
#   '             Z',
#   '             Z',
# ]

# input = [
#   '                   A               ',
#   '                   A               ',
#   '  #################.#############  ',
#   '  #.#...#...................#.#.#  ',
#   '  #.#.#.###.###.###.#########.#.#  ',
#   '  #.#.#.......#...#.....#.#.#...#  ',
#   '  #.#########.###.#####.#.#.###.#  ',
#   '  #.............#.#.....#.......#  ',
#   '  ###.###########.###.#####.#.#.#  ',
#   '  #.....#        A   C    #.#.#.#  ',
#   '  #######        S   P    #####.#  ',
#   '  #.#...#                 #......VT',
#   '  #.#.#.#                 #.#####  ',
#   '  #...#.#               YN....#.#  ',
#   '  #.###.#                 #####.#  ',
#   'DI....#.#                 #.....#  ',
#   '  #####.#                 #.###.#  ',
#   'ZZ......#               QG....#..AS',
#   '  ###.###                 #######  ',
#   'JO..#.#.#                 #.....#  ',
#   '  #.#.#.#                 ###.#.#  ',
#   '  #...#..DI             BU....#..LF',
#   '  #####.#                 #.#####  ',
#   'YN......#               VT..#....QG',
#   '  #.###.#                 #.###.#  ',
#   '  #.#...#                 #.....#  ',
#   '  ###.###    J L     J    #.#.###  ',
#   '  #.....#    O F     P    #.#...#  ',
#   '  #.###.#####.#.#####.#####.###.#  ',
#   '  #...#.#.#...#.....#.....#.#...#  ',
#   '  #.#####.###.###.#.#.#########.#  ',
#   '  #...#.#.....#...#.#.#.#.....#.#  ',
#   '  #.###.#####.###.###.#.#.#######  ',
#   '  #.#.........#...#.............#  ',
#   '  #########.###.###.#############  ',
#   '           B   J   C               ',
#   '           U   P   P               ',
# ]

def is_portal(c):
  return c >= 'A' and c <= 'Z'

def dirs_of(p):
  return [(p[0], p[1] + 1),
          (p[0], p[1] - 1),
          (p[0] + 1, p[1]),
          (p[0] - 1, p[1]),]

items = {}
portals = {}
for y in range(len(input)):
  for x in range(len(input[y])):
    if input[y][x] in [' ', '\n']:
      continue
    if is_portal(input[y][x]):
      ds = [input[y1][x1] for (x1, y1) in dirs_of((x, y)) if x1 >= 0 and y1 >= 0 and len(input) > y1 and len(input[y1]) > x1 if input[y1][x1] != ' ']
      if '.' in ds:
        assert len(ds) == 2
        other = [d for d in ds if d != '.'][0]
        ds = [(x1, y1) for (x1, y1) in dirs_of((x, y)) if x1 >= 0 and y1 >= 0 and len(input) > y1 and len(input[y1]) > x1 if input[y1][x1] == '.']
        assert(len(ds)) == 1
        p_name = other + input[y][x]
        if p_name in portals:
          p_name = ''.join(list(reversed(p_name)))
        portals[p_name] = ds[0]
    else:
      items[(x, y)] = input[y][x]

def steps_to(start, end):

  STACK = [(start, end, 0, [])]

  res = []

  while STACK:
    start, end, total_steps, been = STACK.pop()

    if start == end:
      res.append(total_steps)
      continue

    if items.get(start) not in ['.', '@']:
      continue

    been_now = been + [start]
    for d in dirs_of(start):
      if d not in been:
        if items.get(d) == '.':
          STACK.append((d, end, total_steps+1, been_now))

  return min(res) if res else None

from collections import defaultdict
ptp = defaultdict(list)
for portal, p_loc in portals.items():
  for dest, d_loc in portals.items():
    if dest == portal:
      continue
    if steps := steps_to(p_loc, d_loc):
      ptp[portal].append((dest, steps))

def how_many_to(start, end, been=None):

  if been is None:
    been = []

  been_now = been + [start]

  res = []
  can = ptp[start]
  for can_p, can_s in can:
    if can_p in been_now or ''.join(list(reversed(can_p))) in been_now:
      continue
    if can_p == end:
      res.append((been_now + [can_p], can_s))
    else:
      x = how_many_to(''.join(list(reversed(can_p))), end, been_now)
      if x:
        res.append((x[0], 1 + can_s + x[1]))


  return min(res, key=lambda x: x[1]) if res else None
