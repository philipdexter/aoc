
lines = []
for line in open('input.txt'):
  lines.append([int(x) for x in line.strip().split()])

num = 0
for line in lines:
  bad = False
  if line != sorted(line) and line != sorted(line, reverse=True):
    continue
  for a, b in zip(line, line[1:]):
    if abs(a-b) < 1 or abs(a-b) > 3:
      bad = True
      break
  if bad:
    continue
  num += 1
print(num)
