

def next_scores(a, b):
  c = a + b
  return [int(x) for x in list(str(c))]

scoreboard = [3, 7]

from dataclasses import dataclass
@dataclass
class Elf:
  pos: int

def round():
  global scoreboard
  scoreboard += next_scores(scoreboard[elf_1.pos], scoreboard[elf_2.pos])
  elf_1.pos = (elf_1.pos + 1 + scoreboard[elf_1.pos]) % len(scoreboard)
  elf_2.pos = (elf_2.pos + 1 + scoreboard[elf_2.pos]) % len(scoreboard)

elf_1 = Elf(pos=0)
elf_2 = Elf(pos=1)

import re

input = 939601

def done():
  if scoreboard[-6:] == [9,3,9,6,0,1]:
    print('done')
    print(len(scoreboard[:-6])+1)
    return True
  elif scoreboard[-7:-1] == [9,3,9,6,0,1]:
    print('done 2')
    print(len(scoreboard[:-7]))
    return True
  else:
    return False

print(scoreboard)
while not done():
  round()
