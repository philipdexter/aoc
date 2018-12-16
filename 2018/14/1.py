

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

input = 939601

print(scoreboard)
while len(scoreboard) < 10 + input:
  round()
print(scoreboard[input:][:10])

