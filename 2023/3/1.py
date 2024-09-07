
lines = open('input.txt').read().split('\n')

def is_special(c):
  return c != '.' and c not in '1234567890'

def get(row, char):
  try:
    return lines[row][char]
  except IndexError:
    return '.'

def num_at(row, char):
  line = lines[row][char:] + '...'
  for i, c in enumerate(line):
    if c not in '1234567890':
      break
  return int(line[:i])

def get_surrounding(row, char):
  return [get(row-1, char-1),
          get(row-1, char),
          get(row-1, char+1),
          get(row, char-1),
          get(row, char+1),
          get(row+1, char-1),
          get(row+1, char),
          get(row+1, char+1)]

agg = 0
for row, line in enumerate(lines):
  for char, c in enumerate(line):
    if get(row, char-1) in '1234567890':
      continue
    if c in '1234567890':
      num = num_at(row, char)
      surrounding = []
      for char_, _ in enumerate(str(num)):
        surrounding += get_surrounding(row, char + char_)
      for s in surrounding:
        if is_special(s):
          agg += num
          break
print(agg)
