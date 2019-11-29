input = 'iwrupvqb'

import itertools
import hashlib

for i in itertools.count():
  v = input + str(i)
  h = hashlib.md5(v.encode('utf-8')).hexdigest()
  if h.startswith('00000'):
    print(i)
    exit(0)
