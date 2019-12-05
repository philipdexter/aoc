

with open('1.txt') as f:
  input = f.read().strip()

mem = [int(x) for x in input.split(',')]

def at(*x):
  if len(x) == 1:
    return mem[x[0]]
  return [at(z) for z in x]
def set(x, y):
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
                }

def mode(opcode, i):
  index = 2 + i
  opcode = str(opcode)
  if len(opcode) >= index:
    return int(opcode[-index])
  return 0

def go():
  i = 0
  moded = False
  while True:
    opcode = at(i)

    a_opcode = int(str(opcode)[-2:])

    if a_opcode == 99:
      print('halt')
      return

    num_args = num_args_map[a_opcode]

    args = [at(i+1+j) if mode(opcode, j+1) == 0 else i+1+j for j in range(num_args)]

    if a_opcode == 1:
      add(*args)
    elif a_opcode == 2:
      mul(*args)
    elif a_opcode == 3:
      inpt(*args)
    elif a_opcode == 4:
      outpt(*args)
    elif a_opcode == 5:
      if pc := jit(*args):
        i = pc
        moded = True
      else:
        moded = False
    elif a_opcode == 6:
      if pc := jif(*args):
        i = pc
        moded = True
      else:
        moded = False
    elif a_opcode == 7:
      lt(*args)
    elif a_opcode == 8:
      eq(*args)
    else:
      raise Exception('bad opcode: ' + str(opcode))
    if a_opcode not in [5, 6] or not moded:
      i += 1 + num_args
    if len(mem) <= i:
      print('done')
      return

def get_input():
  print('getting input')
  return 5

def set_output(x):
  print(x)

go()
# print(mem[0])
