
lines = open('input.txt').read().split()

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def line_sum(line):
  a, b = 0, 0
  for i, c in enumerate(line):
    found = False
    for x, num in enumerate(nums):
      if line[i:].startswith(num):
        a = x + 1
        found = True
        break
    if found:
      break
    try:
      a = int(c)
      break
    except:
      continue
  for i, c in enumerate(reversed(line)):
    found = False
    for x, num in enumerate(nums):
      if line[::-1][i:].startswith(num[::-1]):
        b = x + 1
        found = True
        break
    if found:
      break
    try:
      b = int(c)
      break
    except:
      continue
  return int(f'{a}{b}')

print(sum(map(line_sum, lines)))
