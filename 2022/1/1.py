
with open('input.txt') as f:
  lines = f.read().strip().split('\n')


elves = []
cur = []
for line in lines:
  if line == '':
    elves.append(cur)
    cur = []
    continue
  cur.append(int(line))
elves.append(cur)
print(max([sum(xs) for xs in elves]))
