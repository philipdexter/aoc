
with open('1.txt', 'r') as f:
  input = f.read()


def process(w, h, l):
  sides = [l * w, w * h, h * l]
  smallest = min(sides)
  area = sum([2 * side for side in sides])
  return area + smallest

agg = 0
for line in input.split('\n'):
  if not line: continue
  line = map(int, line.strip().split('x'))
  agg += process(*line)

print(agg)
