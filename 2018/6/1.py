
from toolz import frequencies
from toolz.dicttoolz import keyfilter, valfilter
import sys

def man_dist(x, y):
  return abs(x[0]-y[0]) + abs(x[1]-y[1])

def closest(x, y, points):
  point_dists = list(map(lambda p: (p, man_dist((x,y), p)), points))
  # if (x,y) == (1,4):
  #   print(point_dists)
  closest_point, closest_dist = min(point_dists, key=lambda x: x[1])
  dists = list(map(lambda x: x[1], point_dists))
  # if (x,y) == (1,4):
  #   print(dists)
  if dists.count(closest_dist) > 1: return None
  return closest_point

cmap = {}
def parse(line):
  parts = line.split()
  x, y = int(parts[0].rstrip(',')), int(parts[1])
  cmap[(x,y)] = 'A'
  return x, y


points = list(map(parse, sys.stdin))

# find corners
min_x = min(points, key=lambda x: x[0])[0]
min_y = min(points, key=lambda x: x[1])[1]
max_x = max(points, key=lambda x: x[0])[0]
max_y = max(points, key=lambda x: x[1])[1]
grid = {}
for y in range(min_y, max_y+1):
  for x in range(min_x, max_x+1):
    c = closest(x, y, points)
    if c:
      grid[(x,y)] = c
      print(cmap[c], end='')
    else:
      print('.', end='')
  print()
# print(grid)
bad_points = keyfilter(lambda x: x[0] in [max_x, min_x] or x[1] in [max_y, min_y], grid).values()
grid = valfilter(lambda x: x not in bad_points, grid)
# print(grid)
print(max(frequencies(grid.values()).values()))
