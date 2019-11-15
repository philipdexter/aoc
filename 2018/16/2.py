
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

ops = {
  0: 'eqri',
  1: 'bani',
  2: 'seti',
  3: 'bori',
  4: 'eqir',
  5: 'banr',
  6: 'borr',
  7: 'muli',
  8: 'setr',
  9: 'addr',
 10: 'eqrr',
 11: 'addi',
 12: 'gtir',
 13: 'gtrr',
 14: 'gtri',
 15: 'mulr',
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

  for name in to_remove:
    candidates[op].pop(name)

def go():
  with open('2.txt') as f:
    for line in f:
      op, a, b, c = [int(part) for part in line.split()]
      instr = instrs[ops[op]]
      instr(a, b, c)
