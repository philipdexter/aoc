
with open('1.txt') as f:
  input = f.readlines()

input = [line.strip() for line in input]


ll = 10007
deck = list(range(ll))

def process(s):
  parts = s.split()
  if parts == ['deal', 'into', 'new', 'stack']:
    newstack()
  elif parts[:-1] == ['deal', 'with', 'increment']:
    increment(int(parts[-1]))
  else:
    cut(int(parts[-1]))

def newstack():
  global deck
  deck = list(reversed(deck))

def cut(n):
  global deck
  deck = deck[n:] + deck[:n]

def increment(n):
  global deck
  newdeck = list(range(ll))
  for i in range(ll):
    newdeck[(i * n) % ll]= deck[i]
  deck = newdeck

[process(line) for line in input]
