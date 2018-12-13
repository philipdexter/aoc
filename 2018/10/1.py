
from dataclasses import dataclass

@dataclass
class Light:
  pos: (int, int)
  velocity: (int, int)

  def update(self):
    self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

def parse(line):
  parts = line.replace(',', '').replace('<', ' ').replace('>', ' ').split()
  x, y, vx, vy = [int(x) for x in [parts[1], parts[2], parts[4], parts[5]]]
  return Light((x,y), (vx, vy))

import sys
lights = [parse(line) for line in sys.stdin]

grid = {}

def step():
  global grid

  for light in lights:
    light.update()

  grid = {}
  for light in lights:
    grid[(light.pos[0], light.pos[1])] = '*'

def print_grid():
  grid = {}
  for light in lights:
    grid[(light.pos[0], light.pos[1])] = '*'
  min_x = min([light.pos[0] for light in lights])
  max_x = max([light.pos[0] for light in lights])
  min_y = min([light.pos[1] for light in lights])
  max_y = max([light.pos[1] for light in lights])
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      if grid.get((x,y)):
        print(grid[(x, y)], end='')
      else:
        print('.', end='')
    print()

def print_around(x, y):
  for y in range(y-10, y+11):
    for x in range(x-10, x+11):
      print(grid.get((x,y), '.'), end='')
    print()

steps = 0
def check_around(x, y):
  if grid.get((x+1,y)) and grid.get((x-1,y)):
    print_grid()
    print('=================')
    print(steps)
    print('=================')
    return True
  return False
  # count_around = 0
  # for x in range(y-10, y+11):
  #   for y in range(x-10, x+11):
  #     if grid.get((x, y)):
  #       count_around += 1
  #       if count_around >= 15:
  #         print_around(x, y)
  #         print_grid()
  #         exit(0)
  #         return

def check_lines():
  for light in lights:
    if check_around(*light.pos):
      break

while True:
  steps += 1
  step()
  check_lines()
