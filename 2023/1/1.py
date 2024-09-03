
lines = open('input.txt').read().split()

def line_sum(line):
  a, b = 0, 0
  for c in line:
    try:
      a = int(c)
      break
    except:
      continue
  for c in reversed(line):
    try:
      b = int(c)
      break
    except:
      continue
  return int(f'{a}{b}')

print(sum(map(line_sum, lines)))
