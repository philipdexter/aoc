
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

def calc(x, y, size):
  agg = 0
  smaller = group_power_levels.get((x,y,size-1))
  if smaller:
    for a in range(x, x+size):
      agg += grid[(a,y+size-1)]
    for b in range(y, y+size-1):
      agg += grid[(x+size-1, b)]
    if size == 3 and (x,y) == (243,17):
      print(smaller)
      print(agg)
      for a in range(x, x+size):
        for b in range(y, y+size):
          print(grid[(x, y)], end=' ')
        print()
    agg += smaller

  else:
    for a in range(x, x+size):
      for b in range(y, y+size):
        agg += grid[(a,b)]
  return agg

group_power_levels = {}
for size in range(1, 300+1):
  print(f'size {size}')
  for x in range(1,300+1-size):
    for y in range(1,300+1-size):
      group_power_levels[(x,y,size)] = calc(x,y,size)
  print(max(group_power_levels.items(), key=lambda x: x[1]))

print(max(group_power_levels.items(), key=lambda x: x[1]))
