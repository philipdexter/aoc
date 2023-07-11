with open('input.txt') as f:
  lines = f.read().strip().split('\n')

def overlaps(a: int, b: int, c: int, d: int) -> bool:
  return not (a > d or b < c)

num = 0
for line in lines:
  first, second = line.split(',')
  a, b = first.split('-')
  c, d = second.split('-')
  if overlaps(int(a), int(b), int(c), int(d)):
    num += 1
print(num)
