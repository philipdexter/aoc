
import sys

[line] = list(sys.stdin)
line = list(line.rstrip())

def reacts(a, b):
  return a != b and a.lower() == b.lower()

def dead_simple_react(s):
  while True:
    for i, c in enumerate(s):
      if i == len(s) - 1: return
      if reacts(c, s[i+1]):
        del s[i]
        del s[i]
        break

dead_simple_react(line)
print(len(line))
