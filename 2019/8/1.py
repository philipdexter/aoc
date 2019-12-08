
with open('1.txt') as f:
  input = f.read().strip()

width = 25
height = 6

def chunk(ls, num):
  return ls[:num], ls[num:]

layers = []
while input:
  layer = []
  for i in range(height):
    ch, input = chunk(input, width)
    layer.append(ch)
  layers.append([c for l in layer for c in l])
min_zeroes = min(layers, key=lambda x: x.count('0'))
print(min_zeroes.count('1') * min_zeroes.count('2'))
