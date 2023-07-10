
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

def priority(c: str) -> int:
  return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1
assert priority('a') == 1
assert priority('A') == 27

agg = 0
for i in range(0, len(lines), 3):
  line1, line2, line3 = lines[i:i+3]
  in_all = [x for x in line1 if line2.count(x) > 0 and line3.count(x) > 0][0]
  agg += priority(in_all)
print(agg)
