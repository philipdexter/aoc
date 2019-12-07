

with open('1.txt') as f:
  input = f.read().strip()

# input = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
# input = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'

mem = [int(x) for x in input.split(',')]
oldmem = mem[:]

def at(*x):
  if len(x) == 1:
    return mem[x[0]]
  return [at(z) for z in x]
def set(x, y):
  mem[x] = y

def reset():
  global mem
  global gave_phase
  mem = oldmem[:]
  gave_phase = False

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
      # print('halt')
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
  global gave_phase
  if gave_phase:
    # print(f'input {cur_amp} = {output[cur_amp - 1] if cur_amp > 0 else 0}')
    return output[cur_amp - 1] if cur_amp > 0 else 0
  gave_phase = True
  # print(f'input phase {cur_amp} = {phase_setting[cur_amp]}')
  return phase_setting[cur_amp]

def set_output(x):
  # print(f'out {cur_amp} = {x}')
  output[cur_amp] = x

phase_setting = [4, 3, 2, 1, 0]
output = [-1, -1, -1, -1, -1]

cur_amp = 0

gave_phase = False


max_signal = 0

def remove(ls, ds):
  return [x for x in ls if x not in ds]

all_phases = [[a, b, c, d, e]
              for a in range(0, 5)
              for b in remove(list(range(0, 5)), [a])
              for c in remove(list(range(0, 5)), [a,b])
              for d in remove(list(range(0, 5)), [a,b,c])
              for e in remove(list(range(0, 5)), [a,b,c,d])]

for phases in all_phases:
# for phases in range(1):
  phase_setting = phases
  # phase_setting = [4,3,2,1,0]
  # phase_setting = [0, 1, 2, 3, 4]

  for i in range(5):
    cur_amp = i
    # print(f'{cur_amp} --------')
    go()
    # print(output)
    # print(output[-1])
    if output[-1] > max_signal:
      max_signal = output[-1]
    reset()

print(f'{max_signal=}')

# go()
# print(mem[0])
