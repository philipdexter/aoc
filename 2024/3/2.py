
import re

program = open('input.txt').read().strip()

c = re.compile("do\(\)|don't\(\)")

dos = []
donts = []
for match in c.finditer(program):
  command = match[0]
  startpos = match.start()
  if command == 'do()':
    dos.append(startpos)
  else:
    donts.append(startpos)

def on(pos):
  dopos = 0
  dontpos = 0
  if pos < dos[0]:
    dopos = 0
  else:
    for do in dos:
      if pos > do:
        dopos = do
      else:
        break
  if pos < donts[0]:
    dontpos = 0
  else:
    for dont in donts:
      if pos > dont:
        dontpos = dont
      else:
        break
  return dopos >= dontpos

c = re.compile('mul\(([0-9]+),([0-9]+)\)')
groups = c.finditer(program)
x = 0
for match in groups:
  startpos = match.start()
  a = match[1]
  b = match[2]
  if on(startpos):
    x += int(a) * int(b)
print(x)
