
with open('1.txt') as f:
  input = f.readlines()

input = ['157 ORE => 5 NZVS',
         '165 ORE => 6 DCFZ',
         '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
         '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
         '179 ORE => 7 PSHF',
         '177 ORE => 5 HKGWZ',
         '7 DCFZ, 7 PSHF => 2 XJWVT',
         '165 ORE => 2 GPVTF',
         '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT',]

def proc(line):
  start, end = line.split(' => ')
  end = end.split(' ')
  pieces = [piece.split(' ') for piece in start.split(', ')]
  return pieces, end

input = [proc(line.strip()) for line in input]

recipes = {}
for start, end in input:
  recipes[end[1]] = (int(end[0]), [(b, int(a)) for a, b in start])

from collections import defaultdict
leftover = defaultdict(lambda: 0)

def to_get(what, want):
  if what == 'ORE':
    return want
  (gives, pieces) = recipes[what]
  if leftover[what] >= want:
    leftover[what] -= want
    return 0

  if want <= gives:
    if want < gives:
      leftover[what] += gives - want
    return sum([to_get(*piece) for piece in pieces])

  agg = 0
  while want > 0:
    if want > gives:
      agg += to_get(what, gives)
    else:
      agg += to_get(what, want)
    want -= gives
  return agg

for i in range(1000000000000):
  leftover = defaultdict(lambda: 0)
  required = to_get('FUEL', i)
  if i % 1000 == 0:
    print(i)
  if required > 1000000000000:
    print('done: ' + str(i-1))
    break

# ore = 1000000000000
# fuel = 0
# while ore > 0:
#   this = to_get('FUEL', 1)
#   ore -= this
#   if ore >= 0:
#     fuel += 1
#   if fuel % 1000 == 0:
#     print('ore ' + str(ore))
#     print('fuel' + str(fuel))
# print(fuel)
