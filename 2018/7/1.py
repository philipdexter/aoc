
import sys
from toolz.dicttoolz import merge_with, valfilter

def parse(line):
  parts = line.split()
  return (parts[1], parts[7])

pairs = [parse(line) for line in sys.stdin]
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


while len(avail) > 0:
  avail = sorted(avail)
  current = avail[0]
  order += current
  avail = avail[1:]
  avail += filter_avail(d.get(current, []))
  avail = list(set(avail))
print(order)
