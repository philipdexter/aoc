
with open('1.txt') as f:
  input = f.readlines()

# input = [
#   '         A         ',
#   '         A         ',
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
#   '             Z     ',
#   '             Z     ',
# ]

# input = [
#   '             Z L X W       C                 ',
#   '             Z P Q B       K                 ',
#   '  ###########.#.#.#.#######.###############  ',
#   '  #...#.......#.#.......#.#.......#.#.#...#  ',
#   '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ',
#   '  #.#...#.#.#...#.#.#...#...#...#.#.......#  ',
#   '  #.###.#######.###.###.#.###.###.#.#######  ',
#   '  #...#.......#.#...#...#.............#...#  ',
#   '  #.#########.#######.#.#######.#######.###  ',
#   '  #...#.#    F       R I       Z    #.#.#.#  ',
#   '  #.###.#    D       E C       H    #.#.#.#  ',
#   '  #.#...#                           #...#.#  ',
#   '  #.###.#                           #.###.#  ',
#   '  #.#....OA                       WB..#.#..ZH',
#   '  #.###.#                           #.#.#.#  ',
#   'CJ......#                           #.....#  ',
#   '  #######                           #######  ',
#   '  #.#....CK                         #......IC',
#   '  #.###.#                           #.###.#  ',
#   '  #.....#                           #...#.#  ',
#   '  ###.###                           #.#.#.#  ',
#   'XF....#.#                         RF..#.#.#  ',
#   '  #####.#                           #######  ',
#   '  #......CJ                       NM..#...#  ',
#   '  ###.#.#                           #.###.#  ',
#   'RE....#.#                           #......RF',
#   '  ###.###        X   X       L      #.#.#.#  ',
#   '  #.....#        F   Q       P      #.#.#.#  ',
#   '  ###.###########.###.#######.#########.###  ',
#   '  #.....#...#.....#.......#...#.....#.#...#  ',
#   '  #####.#.###.#######.#######.###.###.#.#.#  ',
#   '  #.......#.......#.#.#.#.#...#...#...#.#.#  ',
#   '  #####.###.#####.#.#.#.#.###.###.#.###.###  ',
#   '  #.......#.....#.#...#...............#...#  ',
#   '  #############.#.#.###.###################  ',
#   '               A O F   N                     ',
#   '               A A D   M                     ',
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
recurse = {}
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
        if ds[0][0] <= 2 or ds[0][1] <= 2 or ds[0][0] >= len(input[0]) - 4 or ds[0][1] >= len(input) - 4:
          recurse[p_name] = 1
        else:
          recurse[p_name] = -1
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

max_levels = 25
def how_many_to(start, end, level=0, been=None):

  if been is None:
    been = []

  STACK = [(start, end, level, been, 0)]

  res = []

  while STACK:
    start, end, level, been, agg = STACK.pop()

    if level < -max_levels:
      continue

    if level > 0:
      continue

    been_now = been + [(start, level)]

    can = ptp[start]
    for can_p, can_s in can:
      if (can_p, level) in been_now:
        continue
      if can_p == 'AA':
        continue
      if can_p == end:
        if end == 'ZZ' and level != 0:
          continue
        res.append((been_now + [can_p], agg + can_s))
      else:
        STACK.append((''.join(list(reversed(can_p))), end, level + recurse[can_p], been_now, 1 + can_s + agg))

  return min(res, key=lambda x: x[1]) if res else None
