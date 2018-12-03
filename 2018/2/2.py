from toolz.itertoolz import frequencies
from toolz.dicttoolz import valfilter

def diff_1(a, b):
  if len(a) != len(b):
    print(a)
    print(b)
    print('nope')
    exit(0)
  found = False
  same = []
  for i in range(len(a)):
    if a[i] != b[i]:
      if found:
        return False
      else:
        found = True
        continue
    else:
      same += a[i]
  print(same)
  return found

ss = None
with open('1') as f:
  ss = list(map(lambda x: x.rstrip(), f))

for a in ss:
  for b in ss:
    if a == b:
      continue
    if diff_1(a, b):
      print(a, b)
      exit(0)
