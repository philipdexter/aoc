
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

def priority(c: str) -> int:
  return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1
assert priority('a') == 1
assert priority('A') == 27

agg = 0
for line in lines:
  l = len(line) // 2
  a, b = (line[:l], line[l:])
  assert len(a) == len(b)
  in_both = [c for c in a if b.count(c) > 0][0]
  agg += priority(in_both)
print(agg)
