from collections import Counter

left, right = [], []
for line in open('input.txt'):
  l, r = line.split()
  left.append(int(l))
  right.append(int(r))

right = Counter(right)
total = 0
for l in left:
  total += l * right.get(l, 0)
print(total)
