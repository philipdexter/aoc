

with open('1.txt') as f:
  input = f.read().strip()

global_mem = [int(x) for x in input.split(',')]

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

class pc:

  def __init__(self, address):
    self.address = address
    self.mem = global_mem[:]
    self.q = [address]
    self.oos = [None] * 3
    self.opm = 0

    self.stuck = False

    self.i = 0
    self.rb = 0
    self.moded = False

  def at(self, *x):
    if len(x) == 1:
      if len(self.mem) <= x[0]:
        self.mem = self.mem + ([0] * (1 + x[0] - len(self.mem)))
      return self.mem[x[0]]
    return [self.at(z) for z in x]

  def set(self, x, y):
    if len(self.mem) <= x:
      self.mem = self.mem + ([0] * (1 + x - len(self.mem)))
    self.mem[x] = y

  def add(self, x, y, z):
    self.set(z, self.at(x) + self.at(y))

  def mul(self, x, y, z):
    self.set(z, self.at(x) * self.at(y))

  def inpt(self, x):
    res = self.get_input()
    if res == -1:
      self.stuck = True
    else:
      self.stuck = False
    self.set(x, res)
    return res

  def outpt(self, x):
    self.stuck = False
    self.set_output(self.at(x))

  def jit(self, x, y):
    return self.at(y) if self.at(x) != 0 else None

  def jif(self, x, y):
    return self.at(y) if self.at(x) == 0 else None

  def lt(self, x, y, z):
    self.set(z, int(self.at(x) < self.at(y)))

  def eq(self, x, y, z):
    self.set(z, int(self.at(x) == self.at(y)))

  def adj(self, x):
    return self.at(x)

  def go(self):
    opcode = self.at(self.i)

    a_opcode = int(str(opcode)[-2:])

    if a_opcode == 99:
      print('halt')
      return

    num_args = num_args_map[a_opcode]

    def proc_mode(opcode, j):
      m = mode(opcode, j + 1)
      if m == 0:
        return self.at(self.i + 1 + j)
      elif m == 1:
        return self.i + 1 + j
      return self.rb + self.at(self.i + 1 + j)
    args = [proc_mode(opcode, j) for j in range(num_args)]

    if a_opcode == 1:
      self.add(*args)
    elif a_opcode == 2:
      self.mul(*args)
    elif a_opcode == 3:
      res = self.inpt(*args)
    elif a_opcode == 4:
      self.outpt(*args)
    elif a_opcode == 5:
      pc = self.jit(*args)
      if pc is not None:
        self.i = pc
        self.moded = True
      else:
        self.moded = False
    elif a_opcode == 6:
      pc = self.jif(*args)
      if pc is not None:
        self.i = pc
        self.moded = True
      else:
        self.moded = False
    elif a_opcode == 7:
      self.lt(*args)
    elif a_opcode == 8:
      self.eq(*args)
    elif a_opcode == 9:
      d = self.adj(*args)
      self.rb += d
    else:
      raise Exception('bad opcode: ' + str(opcode))
    if a_opcode not in [5, 6] or not self.moded:
      self.i += 1 + num_args
    if len(self.mem) <= self.i:
      print('done')
      return

    return self.stuck

  def get_input(self):
    if self.q:
      return self.q.pop()
    return -1

  def set_output(self, x):
    self.oos[self.opm] = x
    self.opm += 1
    if self.opm == 3:
      self.opm = 0
      if self.oos[0] == 255:
        nat_send(*self.oos[1:])
      else:
        cpus[self.oos[0]].q = [self.oos[2], self.oos[1]] + cpus[self.oos[0]].q
      self.oos = [None] * 3

nat_vals = [None] * 2
def nat_send(x, y):
  global nat_vals
  nat_vals = [x, y]

cpus = {i: pc(i) for i in range(50)}
wait_count = 0
sent = set()
while True:
  stucks = [cpu.go() for cpu in cpus.values()]
  if all(stucks):
    wait_count += 1
    if wait_count > 100:
      assert len(cpus[0].q) == 0
      cpus[0].q = [nat_vals[1], nat_vals[0]]
      if nat_vals[1] in sent:
        print(nat_vals[1])
        exit(0)
      sent.add(nat_vals[1])
      wait_count = 0
  else:
    wait_count = 0
