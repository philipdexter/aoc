
with open('1.txt') as f:
  input = f.readlines()

def calc(x):
  fuel = x // 3 - 2
  if fuel <= 0: return 0
  return fuel + calc(fuel)

agg = 0
for line in input:
  line = line.strip()
  if not line: continue
  agg += calc(int(line))
print(agg)
