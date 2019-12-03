

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

set(1, 12)
set(2, 2)


def go():
  i = 0
  while True:
    opcode = at(i)
    if opcode == 99:
      print('halt')
      return
    elif opcode == 1:
      add(*at(i+1, i+2, i+3))
    elif opcode == 2:
      mul(*at(i+1, i+2, i+3))
    else:
      print('bad opcode: ' + str(opcode))
      return
    i += 4
    if len(mem) <= i:
      print('done')
      return

go()
print(mem[0])
