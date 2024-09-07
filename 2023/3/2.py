
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

def is_num(c):
  return c in '1234567890'

def get_right(row, char):
  return num_at(row, char)

def get_left(row, char):
  for char_ in range(char, -1, -1):
    if not is_num(get(row, char_-1)):
      break
  return num_at(row, char_)

def get_surrounding(row, char):
  right = get_right(row, char+1) if is_num(get(row, char+1)) else None
  left = get_left(row, char) if is_num(get(row, char-1)) else None
  if is_num(get(row-1, char)):
    up = [get_left(row-1, char)]
  else:
    up = [get_left(row-1, char-1) if is_num(get(row-1, char-1)) else None, get_right(row-1, char+1) if is_num(get(row-1, char+1)) else None]
  if is_num(get(row+1, char)):
    down = [get_left(row+1, char)]
  else:
    down = [get_left(row+1, char-1) if is_num(get(row+1, char-1)) else None, get_right(row+1, char+1) if is_num(get(row+1, char+1)) else None]
  return [x for x in ([right, left] + up + down) if x is not None]

agg = 0
for row, line in enumerate(lines):
  for char, c in enumerate(line):
    if c == '*':
      surrounding = get_surrounding(row, char)
      if len(surrounding) == 2:
        agg += surrounding[0] * surrounding[1]
print(agg)
