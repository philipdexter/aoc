
with open('1.txt') as f:
  input = f.read().strip()

offset = int(input[:7])
xs = [int(c) for c in input]
xs = xs * 10000
l = len(xs)

wave = [0, 1, 0, -1]

from itertools import cycle, islice, repeat

def ph(i):
  print(i)
  return islice(cycle((y for x in wave for y in repeat(x, i))), 1, None)

def parts(phase, size):
  print(phase)
  agg = []
  sign = 1
  t = 0
  pos = 0
  while pos <= size:
    if t == 1:
      agg += [(pos + i - 1, sign) for i in range(phase)]
      t = 0
      sign = -sign
    else:
      t = 1
    pos += phase
  return agg

phases = 100
for z in range(phases):
  print(z)
  # xs = [abs(sum([a*b for a, b in zip(xs, ph(i+1))])) % 10 for i in range(len(xs))]
  xs = [abs(sum(xs[a] if b == 1 else -xs[a] for a, b in parts(i+1, l) if a < l)) % 10 for i in range(l)]
print(xs)
print(xs[offset:offset+8])
