
with open('1.txt', 'r') as f:
  input = f.read().strip()



def nice(s):
  vowels = 0
  row = 0

  prev = None
  for c in s:
    if c in "aeiou":
      vowels += 1
    if prev and prev == c:
      row += 1
    prev = c

  return row >= 1 and vowels >= 3 and 'ab' not in s and 'cd' not in s and 'pq' not in s and 'xy' not in s

agg = 0
for line in input.split('\n'):
  if not line: continue
  if nice(line):
    agg += 1

print(agg)
