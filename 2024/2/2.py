
lines = []
for line in open('input.txt'):
  lines.append([int(x) for x in line.strip().split()])

def safe(line):
  bad = False
  if line != sorted(line) and line != sorted(line, reverse=True):
    return False
  for a, b in zip(line, line[1:]):
    if abs(a-b) < 1 or abs(a-b) > 3:
      return False
  return True


def without(line, index):
  line = line[:]
  del line[index]
  return line

num = 0
for line in lines:
  if safe(line):
    num += 1
  else:
    for i in range(len(line)):
      if safe(without(line, i)):
        num += 1
        break
print(num)
