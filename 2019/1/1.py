
with open('1.txt') as f:
  input = f.readlines()

def calc(x):
  return x // 3 - 2

agg = 0
for line in input:
  line = line.strip()
  if not line: continue
  agg += calc(int(line))
print(agg)
