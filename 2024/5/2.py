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

def order(pages):
  correct = []
  def one():
    nonlocal correct
    for i, page in enumerate(pages):
      bs = before[page]
      nobefore = all([b not in pages for b in bs])
      if nobefore or page not in before:
        correct = [page] + correct
        del pages[i]
        break
  while pages:
    one()
  return correct

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
  if fail:
    correct = order(pages)
    num += int(correct[len(correct)//2])
print(num)
