from toolz.itertoolz import frequencies
from toolz.dicttoolz import valfilter

def ex_two(s):
  f = frequencies(s)
  return len(valfilter(lambda x: x == 2, f)) > 0

def ex_three(s):
  f = frequencies(s)
  return len(valfilter(lambda x: x == 3, f)) > 0

ss = None
with open('1') as f:
  ss = list(map(lambda x: x.rstrip(), f))
twos = len(list(filter(ex_two, ss)))
threes = len(list(filter(ex_three, ss)))
print(twos * threes)
