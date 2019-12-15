

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

# set(1, 12)
# set(2, 2)

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
      try:
        inpt(*args)
      except:
        return
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

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
opposite = {NORTH: SOUTH,
            SOUTH: NORTH,
            EAST: WEST,
            WEST: EAST}

pos = (0, 0)
next_pos = (0, 0)
items = {}
ogs = None

to_explore = []

m = 0

moving = {NORTH: 'NORTH',
          SOUTH: 'SOUTH',
          EAST: 'EAST',
          WEST: 'WEST'}

popped = False

def get_input():
  global next_pos
  global m
  global popped

  popped = False

  # ch = getch()
  # if ch == 'h':
  #   m = WEST
  # elif ch == 'j':
  #   m = SOUTH
  # elif ch == 'k':
  #   m = NORTH
  # elif ch == 'l':
  #   m = EAST
  # elif ch == 'q':
  #   exit(0)

  if items.get((pos[0], pos[1] - 1)) is None:
    m = NORTH
  elif items.get((pos[0], pos[1] + 1)) is None:
    m = SOUTH
  elif items.get((pos[0] - 1, pos[1])) is None:
    m = WEST
  elif items.get((pos[0] + 1, pos[1])) is None:
    m = EAST
  else:
    m = to_explore.pop()
    popped = True

  print(f'moving {moving[m]}')

  if m == NORTH:
    next_pos = (pos[0], pos[1] - 1)
  elif m == SOUTH:
    next_pos = (pos[0], pos[1] + 1)
  elif m == EAST:
    next_pos = (pos[0] + 1, pos[1])
  elif m == WEST:
    next_pos = (pos[0] - 1, pos[1])
  else:
    raise Exception('bad dir')
  return m

def set_output(x):
  global pos
  global ogs
  if x == 0:
    print(f'wall at {next_pos}')
    items[next_pos] = '#'
  elif x == 1:
    if not popped:
      to_explore.append(opposite[m])
    if items.get(pos) != 'O':
      items[pos] = '.'
    pos = next_pos
  elif x == 2:
    if not popped:
      to_explore.append(opposite[m])
    if items.get(pos) != 'O':
      items[pos] = '.'
    pos = next_pos
    ogs = pos
    items[pos] = 'O'
    print(f'FOUND {pos}')
    # exit(0)
  print(f'cur pos {pos}')

  print('\033[H')
  if items:
    minx = min(items.keys(), key=lambda x: x[0])[0]
    miny = min(items.keys(), key=lambda x: x[1])[1]
    maxx = max(items.keys(), key=lambda x: x[0])[0]
    maxy = max(items.keys(), key=lambda x: x[1])[1]
    for y in range(minx - 5, maxx + 5):
      for x in range(miny - 5, maxy + 5):
        if (x, y) == (0, 0):
          print('X', end='')
        elif (x, y) == pos:
          print('D', end='')
        elif i := items.get((x, y)):
          print(i, end='')
        else:
          print(' ', end='')
      print()

go()

def fill():
  filled = [ogs]
  time = 0
  while not all([items[i] in [' ', '#', 'O'] for i in items]):
    time += 1
    to_add = []
    for f in filled:
      if items.get((f[0], f[1] - 1)) in ['.', 'X']:
        items[(f[0], f[1] - 1)] = 'O'
        to_add.append((f[0], f[1] - 1))
      if items.get((f[0], f[1] + 1)) in ['.', 'X']:
        items[(f[0], f[1] + 1)] = 'O'
        to_add.append((f[0], f[1] + 1))
      if items.get((f[0] - 1, f[1])) in ['.', 'X']:
        items[(f[0] - 1, f[1])] = 'O'
        to_add.append((f[0] - 1, f[1]))
      if items.get((f[0] + 1, f[1])) in ['.', 'X']:
        items[(f[0] + 1, f[1])] = 'O'
        to_add.append((f[0] + 1, f[1]))
    filled += to_add

    print('\033[H')
    minx = min(items.keys(), key=lambda x: x[0])[0]
    miny = min(items.keys(), key=lambda x: x[1])[1]
    maxx = max(items.keys(), key=lambda x: x[0])[0]
    maxy = max(items.keys(), key=lambda x: x[1])[1]
    for y in range(minx - 5, maxx + 5):
      for x in range(miny - 5, maxy + 5):
        if i := items.get((x, y)):
          print(i, end='')
        else:
          print(' ', end='')
      print()
  print(time)
fill()
