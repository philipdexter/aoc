
from dataclasses import dataclass

@dataclass
class moon:
  x: int
  y: int
  z: int
  vel_x: int = 0
  vel_y: int = 0
  vel_z: int = 0

moons = [moon(x=-7, y=-1, z=6),
         moon(x=6, y=-9, z=-9),
         moon(x=-12, y=2, z=-7),
         moon(x=4, y=-17, z=-12)]

def apply_gravity():
  for moon in moons:
    for other in moons:
      if moon == other: continue
      if moon.x != other.x:
        dir = 1 if moon.x < other.x else -1
        moon.vel_x += dir
      if moon.y != other.y:
        dir = 1 if moon.y < other.y else -1
        moon.vel_y += dir
      if moon.z != other.z:
        dir = 1 if moon.z < other.z else -1
        moon.vel_z += dir

def apply_move():
  for moon in moons:
    moon.x += moon.vel_x
    moon.y += moon.vel_y
    moon.z += moon.vel_z

def step():
  apply_gravity()
  apply_move()

def energy(moon):
  return (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z))

for i in range(1000):
  step()
print(sum([energy(moon) for moon in moons]))
