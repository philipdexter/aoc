
import sys
from toolz.dicttoolz import merge_with, valfilter

def parse(line):
  parts = line.split()
  return (parts[1], parts[7])

pairs = [parse(line) for line in open('1')]
d = merge_with(lambda x: [z for y in x for z in y], *map(lambda x: dict([(x[0], [x[1]])]), pairs))
print(d)
avail = ''.join(list(d.keys()))
print(avail)
for v in d.values():
  for c in v:
    avail = avail.replace(c, '')

avail = sorted(avail)
order = ''
current = ''

def filter_avail(s):
  out = []
  for x in s:
    pres = list(valfilter(lambda y: x in y, d).keys())
    good = True
    for p in pres:
      if p not in order:
        good = False
        break
    if good:
      out.append(x)
  return out

def time_for(c):
  return 60 + ord(c) - ord('A') + 1

working_on = []
second = 0
while len(avail) > 0 or len(working_on) > 0:
  # import pdb ; pdb.set_trace()
  if len(working_on) > 0:
    working_on = [(c, time-1) for c, time in working_on]
    to_remove = []
    for c, time in working_on:
      if time == 0:
        to_remove.append(c)
        order += c
        avail += filter_avail(d.get(c, []))
        avail = list(set(avail))
    working_on = [(c, time) for c, time in working_on if c not in to_remove]

  while len(avail) > 0 and len(working_on) < 5:
    avail = sorted(avail)
    current = avail[0]
    avail = avail[1:]
    working_on.append((current, time_for(current)))

  print(working_on)
  second += 1

print(order)
print(second)
