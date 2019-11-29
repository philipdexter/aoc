
from dataclasses import dataclass

@dataclass
class Unit:
  hp: int

  def rep(self): return 'X'
  def targetable(self): return True
  def walkable(self): return False

@dataclass
class Wall:
  def rep(self): return '#'
  def targetable(self): return False
  def walkable(self): return False

@dataclass
class Floor:
  def rep(self): return '.'
  def targetable(self): return False
  def walkable(self): return True


def parse(c):
  if c == '.':
    return Floor()
  elif c == '#':
    return Wall()
  elif c in ['G', 'E']:
    return Unit(hp=1)

def print_grid():
  for line in grid:
    for c in line:
      print(c.rep(), end='')
    print()

grid = []
import sys
for line in open(sys.argv[1]):
  grid.append([parse(c) for c in list(line.strip())])

max_y = len(grid)
max_x = len(grid[0])

print_grid()

def in_range(pos, r):
  x, y = pos
  to_check = 
  potential_targets = [((a,b), grid[a][b]) for a,b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]]
  return [c for c in potential_targets if c[1].targetable()]

def in_walkable(pos):
  x, y = pos
  potential_squares = [((a,b), grid[a][b]) for a,b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]]
  return [c for c in potential_squares if c[1].walkable()]

def step():
  for y, line in enumerate(grid):
    for x, c in enumerate(line):
      if isinstance(c, Unit):
        in_my_range = in_range((x,y), 1)
        if in_my_range:
          print('attack')
          continue
        targets = in_range((x,y), 4)
        walkable = [in_walkable(target[0])[0] for target in targets]
        if targets:
          print('walk')
          continue
