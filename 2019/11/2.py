

with open('1.txt') as f:
  input = f.read().strip()

mem = [int(x) for x in input.split(',')]

def at(*x):
  global mem
  if len(x) == 1:
    if len(mem) <= x[0]:
      mem = mem + ([0] * (1 + x[0] - len(mem)))
    return mem[x[0]]
  return [at(z) for z in x]
def set(x, y):
  global mem
  if len(mem) <= x:
    mem = mem + ([0] * (1 + x - len(mem)))
  mem[x] = y

def add(x, y, z):
  set(z, at(x) + at(y))

def mul(x, y, z):
  set(z, at(x) * at(y))

def inpt(x):
  set(x, get_input())

def outpt(x):
  set_output(at(x))

def jit(x, y):
  return at(y) if at(x) != 0 else None

def jif(x, y):
  return at(y) if at(x) == 0 else None

def lt(x, y, z):
  set(z, int(at(x) < at(y)))

def eq(x, y, z):
  set(z, int(at(x) == at(y)))

def adj(x):
  return at(x)

num_args_map = {1: 3,
                2: 3,
                3: 1,
                4: 1,
                5: 2,
                6: 2,
                7: 3,
                8: 3,
                9: 1,
                }

def mode(opcode, i):
  index = 2 + i
  opcode = str(opcode)
  if len(opcode) >= index:
    return int(opcode[-index])
  return 0

def go():
  i = 0
  rb = 0
  moded = False
  while True:
    opcode = at(i)

    a_opcode = int(str(opcode)[-2:])

    if a_opcode == 99:
      print('halt')
      return

    num_args = num_args_map[a_opcode]

    def proc_mode(opcode, j):
      m = mode(opcode, j + 1)
      if m == 0:
        return at(i + 1 + j)
      elif m == 1:
        return i + 1 + j
      return rb + at(i + 1 + j)
    args = [proc_mode(opcode, j) for j in range(num_args)]

    if a_opcode == 1:
      add(*args)
    elif a_opcode == 2:
      mul(*args)
    elif a_opcode == 3:
      inpt(*args)
    elif a_opcode == 4:
      outpt(*args)
    elif a_opcode == 5:
      pc = jit(*args)
      if pc is not None:
        i = pc
        moded = True
      else:
        moded = False
    elif a_opcode == 6:
      pc = jif(*args)
      if pc is not None:
        i = pc
        moded = True
      else:
        moded = False
    elif a_opcode == 7:
      lt(*args)
    elif a_opcode == 8:
      eq(*args)
    elif a_opcode == 9:
      d = adj(*args)
      rb += d
    else:
      raise Exception('bad opcode: ' + str(opcode))
    if a_opcode not in [5, 6] or not moded:
      i += 1 + num_args
    if len(mem) <= i:
      print('done')
      return

tiles = {}
tiles[(0, 0)] = 1
pos = (0, 0)
dir = (0, 1)

def turn(s):
  global dir
  if s == 0:
    if dir == (0, 1):
      dir = (-1, 0)
    elif dir == (-1, 0):
      dir = (0, -1)
    elif dir == (0, -1):
      dir = (1, 0)
    else:
      dir = (0, 1)
  else:
    if dir == (0, 1):
      dir = (1, 0)
    elif dir == (1, 0):
      dir = (0, -1)
    elif dir == (0, -1):
      dir = (-1, 0)
    else:
      dir = (0, 1)

def get_input():
  return tiles.get(pos, 0)

paint_output = True
def set_output(x):
  global pos
  global paint_output
  assert x in [0, 1]
  if paint_output:
    tiles[pos] = x
    paint_output = False
  else:
    turn(x)
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    paint_output = True

go()
print(len(tiles))

keys = list(tiles.keys())
minx = min(keys, key=lambda x: x[0])[0]
maxx = max(keys, key=lambda x: x[0])[0]
miny = min(keys, key=lambda x: x[1])[1]
maxy = max(keys, key=lambda x: x[1])[1]
for y in range(maxy+5, miny-5+1, -1):
  for x in range(minx-5, maxx+1+5):
    p = tiles.get((x, y), 0)
    print('.' if p == 0 else '#', end='')
  print()
