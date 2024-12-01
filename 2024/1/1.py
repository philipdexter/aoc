
left, right = [], []
for line in open('input.txt'):
  l, r = line.split()
  left.append(int(l))
  right.append(int(r))

left.sort()
right.sort()
total = 0
for l, r in zip(left, right):
  total += abs(r-l)
print(total)
