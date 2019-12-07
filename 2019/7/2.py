

with open('1.txt') as f:
  input = f.read().strip()

mem = [int(x) for x in input.split(',')]
oldmem = mem[:]

from dataclasses import dataclass
from typing import List

NEED_INPUT = 0
HALT = 1

def mode(opcode, i):
  index = 2 + i
  opcode = str(opcode)
  if len(opcode) >= index:
    return int(opcode[-index])
  return 0

@dataclass
class amp:
  mem: List[int]
  inputs: List[int]
  outputs: List[int]
  pc: int

  def at(self, *x):
    if len(x) == 1:
      return self.mem[x[0]]
    return [self.at(z) for z in x]
  def set(self, x, y):
    self.mem[x] = y

  def add(self, x, y, z):
    self.set(z, self.at(x) + self.at(y))

  def mul(self, x, y, z):
    self.set(z, self.at(x) * self.at(y))

  def inpt(self, x):
    self.set(x, self.inputs[0])
    self.inputs = self.inputs[1:]

  def outpt(self, x):
    self.outputs.append(self.at(x))

  def jit(self, x, y):
    return self.at(y) if self.at(x) != 0 else None

  def jif(self, x, y):
    return self.at(y) if self.at(x) == 0 else None

  def lt(self, x, y, z):
    self.set(z, int(self.at(x) < self.at(y)))

  def eq(self, x, y, z):
    self.set(z, int(self.at(x) == self.at(y)))

  def go(self):
    moded = False
    while True:
      opcode = self.at(self.pc)

      a_opcode = int(str(opcode)[-2:])

      if a_opcode == 99:
        return HALT

      num_args = num_args_map[a_opcode]

      args = [self.at(self.pc+1+j) if mode(opcode, j+1) == 0 else self.pc+1+j for j in range(num_args)]

      if a_opcode == 1:
        self.add(*args)
      elif a_opcode == 2:
        self.mul(*args)
      elif a_opcode == 3:
        if self.inputs:
          self.inpt(*args)
        else:
          return NEED_INPUT
      elif a_opcode == 4:
        self.outpt(*args)
      elif a_opcode == 5:
        if pc := self.jit(*args):
          self.pc = pc
          moded = True
        else:
          moded = False
      elif a_opcode == 6:
        if pc := self.jif(*args):
          self.pc = pc
          moded = True
        else:
          moded = False
      elif a_opcode == 7:
        self.lt(*args)
      elif a_opcode == 8:
        self.eq(*args)
      else:
        raise Exception('bad opcode: ' + str(opcode))
      if a_opcode not in [5, 6] or not moded:
        self.pc += 1 + num_args
      if len(mem) <= self.pc:
        print('out of mem')
        return

num_args_map = {1: 3,
                2: 3,
                3: 1,
                4: 1,
                5: 2,
                6: 2,
                7: 3,
                8: 3,
                }

def remove(ls, ds):
  return [x for x in ls if x not in ds]

all_phases = [[a, b, c, d, e]
              for a in range(5, 10)
              for b in remove(list(range(5, 10)), [a])
              for c in remove(list(range(5, 10)), [a,b])
              for d in remove(list(range(5, 10)), [a,b,c])
              for e in remove(list(range(5, 10)), [a,b,c,d])]

max_signal = 0

# for phase_setting in all_phases:
for phase_setting in all_phases:

  amps = [amp(mem=mem[:], inputs=[phase_setting[i]], outputs=[], pc=0) for i in range(5)]
  amps[0].inputs.append(0)

  halted = [False, False, False, False, False]

  while not all(halted):
    for i in range(5):
      ret = amps[i].go()
      if ret == HALT:
        halted[i] = True
      elif ret == NEED_INPUT:
        prev = (i + 5 - 1) % 5
        if amps[prev].outputs:
          amps[i].inputs = amps[prev].outputs[:]
          amps[prev].outputs = []
      else:
        raise Exception(f'bad ret {ret}')

  assert len(amps[-1].outputs) == 1
  if amps[-1].outputs[0] > max_signal:
    max_signal = amps[-1].outputs[-1]

print(f'{max_signal=}')

# go()
# print(mem[0])
