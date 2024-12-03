
import re

program = open('input.txt').read().strip()
c = re.compile('mul\(([0-9]+),([0-9]+)\)')
groups = c.findall(program)
x = 0
for a, b in groups:
  x += int(a) * int(b)
print(x)
