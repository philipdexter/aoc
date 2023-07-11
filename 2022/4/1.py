with open('input.txt') as f:
  lines = f.read().strip().split('\n')

def fully_contains(a: int, b: int, c: int, d: int) -> bool:
  return a >= c and b <= d or c >= a and d <= b

num = 0
for line in lines:
  first, second = line.split(',')
  a, b = first.split('-')
  c, d = second.split('-')
  if fully_contains(int(a), int(b), int(c), int(d)):
    num += 1
print(num)
