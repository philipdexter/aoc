
grid_serial = 7347

def power_level(x, y):
  rack_id = x + 10
  power_level = rack_id * y
  power_level += grid_serial
  power_level *= rack_id
  power_level = int(str(power_level)[len(str(power_level))-3])
  power_level -= 5
  return power_level

grid = {}
for x in range(1,300+1):
  for y in range(1,300+1):
    grid[(x,y)] = power_level(x,y)

def calc(x, y):
  agg = 0
  for a in [x, x+1, x+2]:
    for b in [y, y+1, y+2]:
      agg += grid[(a,b)]
  return agg

group_power_levels = {}
for x in range(1,300+1-3):
  for y in range(1,300+1-3):
    group_power_levels[(x,y)] = calc(x,y)

print(max(group_power_levels.items(), key=lambda x: x[1]))
