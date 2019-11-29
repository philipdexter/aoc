
with open('1.txt', 'r') as f:
  input = f.read().strip()

import re

def nice(s):
  return bool(re.search(r'(.)(.).*\1\2', s)) and bool(re.search(r'(.).\1', s))

agg = 0
for line in input.split('\n'):
  if not line: continue
  if nice(line):
    agg += 1

print(agg)
