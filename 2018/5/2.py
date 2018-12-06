
import sys

[line] = list(sys.stdin)
line = list(line.rstrip())

def reacts(a, b):
  return a != b and a.lower() == b.lower()

def dead_simple_react(s):
  while True:
    for i, c in enumerate(s):
      if i == len(s) - 1: return s
      if reacts(c, s[i+1]):
        del s[i]
        del s[i]
        break
  return s

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(min([len(dead_simple_react(line[:], letter)) for letter in letters]))

def handle_type(line, letter):
  not_type = list(filter(lambda x: x.lower() != letter, line))
  line = dead_simple_react(not_type)
  return len(line)
print(min([handle_type(line[:], letter) for letter in letters]))
