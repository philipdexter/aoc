

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

input_type = 0

def get_input():
  if ball[0] < paddle[0]:
    print('INPUT -1')
    return -1
  elif ball[0] > paddle[0]:
    print('INPUT 1')
    return 1
  print('INPUT 0')
  return 0

input_type = 0
pos_x = 0
pos_y = 0

items = {}
ball = (0, 0)
paddle = (0, 0)
score = 0

def set_output(x):
  global input_type
  global pos_x
  global pos_y
  global blocks
  global ball
  global paddle
  global score
  if input_type == 0:
    pos_x = x
  elif input_type == 1:
    pos_y = x
  else:
    if pos_x == -1 and pos_y == 0:
      score = x
    elif x == 2:
      assert (pos_x, pos_y) not in items
      items[(pos_x, pos_y)] = 'B'
    elif x == 3:
      assert (pos_x, pos_y) not in items
      items[(pos_x, pos_y)] = '_'
      paddle = (pos_x, pos_y)
    elif x == 4:
      assert (pos_x, pos_y) not in items
      items[(pos_x, pos_y)] = 'O'
      ball = (pos_x, pos_y)
    elif x == 1:
      assert (pos_x, pos_y) not in items
      items[(pos_x, pos_y)] = '|'
    elif x == 0:
      # assert (pos_x, pos_y) in items
      if (pos_x, pos_y) in items:
        items.pop((pos_x, pos_y))

  input_type += 1
  input_type %= 3
  assert input_type in [0, 1, 2]

  if items:
    print('\033[H')
    for y in range(0, 5 + max(items.keys(), key=lambda x: x[1])[1]):
      for x in range(0, 5 + max(items.keys(), key=lambda x: x[0])[0]):
        if c := items.get((x, y)):
          print(c, end='')
        else:
          print(' ', end='')
      print()

set(0, 2)

go()
print(score)
