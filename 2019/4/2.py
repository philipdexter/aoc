
input = range(137683, 596253)


import re
r = re.compile(r'((.)\2+)')

def match(n):
  s = str(n)
  prev = None
  for c in s:
    if prev:
      if prev > int(c):
        return False
    prev = int(c)
  if matches := r.findall(s):
    if all([len(a) != 2 for a, b in matches]):
      return False
  else:
    return False

  return True

agg = 0
for n in input:
  if  match(n):
    agg += 1

print(agg)
