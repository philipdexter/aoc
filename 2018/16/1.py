
import copy
import sys

regs = [0, 0, 0, 0]

def addi(a, b, c):
  regs[c] = regs[a] + b
def addr(a, b, c):
  regs[c] = regs[a] + regs[b]
def muli(a, b, c):
  regs[c] = regs[a] * b
def mulr(a, b, c):
  regs[c] = regs[a] * regs[b]
def bani(a, b, c):
  regs[c] = regs[a] & b
def banr(a, b, c):
  regs[c] = regs[a] & regs[b]
def bori(a, b, c):
  regs[c] = regs[a] | b
def borr(a, b, c):
  regs[c] = regs[a] | regs[b]
def seti(a, b, c):
  regs[c] = a
def setr(a, b, c):
  regs[c] = regs[a]
def gtir(a, b, c):
  regs[c] = 1 if a > regs[b] else 0
def gtri(a, b, c):
  regs[c] = 1 if regs[a] > b else 0
def gtrr(a, b, c):
  regs[c] = 1 if regs[a] > regs[b] else 0
def eqir(a, b, c):
  regs[c] = 1 if a == regs[b] else 0
def eqri(a, b, c):
  regs[c] = 1 if regs[a] == b else 0
def eqrr(a, b, c):
  regs[c] = 1 if regs[a] == regs[b] else 0

instrs = {
    'addi': addi,
    'addr': addr,
    'muli': muli,
    'mulr': mulr,
    'bani': bani,
    'banr': banr,
    'bori': bori,
    'borr': borr,
    'seti': seti,
    'setr': setr,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
   }

candidates = {
  0: copy.deepcopy(instrs),
  1: copy.deepcopy(instrs),
  2: copy.deepcopy(instrs),
  3: copy.deepcopy(instrs),
  4: copy.deepcopy(instrs),
  5: copy.deepcopy(instrs),
  6: copy.deepcopy(instrs),
  7: copy.deepcopy(instrs),
  8: copy.deepcopy(instrs),
  9: copy.deepcopy(instrs),
  10: copy.deepcopy(instrs),
  11: copy.deepcopy(instrs),
  12: copy.deepcopy(instrs),
  13: copy.deepcopy(instrs),
  14: copy.deepcopy(instrs),
  15: copy.deepcopy(instrs),
  }

def try_instr(instr, before, after):
  global regs
  old_regs = regs

  op, a, b, c = instr

  to_remove = []
  for name, instr in candidates[op].items():
    regs = before[:]
    instr(a, b, c)
    if regs != after:
      to_remove.append(name)

  regs = old_regs

  #for name in to_remove:
  #  candidates[op].pop(name)

  return 1 if len(to_remove) <= 13 else 0

def go():
  with open('1.txt') as f:
    total = 0
    for line in f:
      before, instr, after = [[int(part) for part in parts.split()] for parts in line.split(' - ')]
      total += try_instr(instr, before, after)
    print(total)
