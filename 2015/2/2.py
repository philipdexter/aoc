
with open('1.txt', 'r') as f:
  input = f.read()


def process(w, h, l):
  dims = [w, h, l]
  small1 = min(dims)
  dims.remove(small1)
  small2 = min(dims)
  return w*h*l + 2*small1 + 2*small2

agg = 0
for line in input.split('\n'):
  if not line: continue
  line = map(int, line.strip().split('x'))
  agg += process(*line)

print(agg)
