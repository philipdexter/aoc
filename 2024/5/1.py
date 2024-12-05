from collections import defaultdict

rules = []
updates = []
which = True
for line in open('input.txt'):
  line = line.strip()
  if not line:
    which = False
    continue
  if which:
    rules.append(line)
  else:
    updates.append(line)

before = defaultdict(list)
for rule in rules:
  a, b = rule.split('|')
  before[a].append(b)

num = 0
for update in updates:
  pages = update.split(',')
  seen = []
  fail = False
  for page in pages:
    for b in before[page]:
      if b in seen:
        fail = True
        break
    seen.append(page)
    if fail:
      break
  if not fail:
    num += int(pages[len(pages)//2])
print(num)
