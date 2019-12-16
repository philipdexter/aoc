
with open('1.txt') as f:
  input = f.read().strip()

xs = [int(c) for c in input]

wave = [0, 1, 0, -1]

from itertools import cycle, islice, repeat

def ph(i):
  return islice(cycle((y for x in wave for y in repeat(x, i))), 1, None)


phases = 100
for _ in range(phases):
  xs = [abs(sum([a*b for a, b in zip(xs, ph(i+1))])) % 10 for i in range(len(xs))]
print(xs)
