
with open('1.txt') as f:
  input = f.read().strip()

width = 25
height = 6

# input = '0222112222120000'
# width = 2
# height = 2

def chunk(ls, num):
  return ls[:num], ls[num:]

layers = []
while input:
  layer = []
  for i in range(height):
    ch, input = chunk(input, width)
    layer.append(ch)
  layers.append([c for l in layer for c in l])

out = []
for i in range(len(layers[0])):
  for j in range(len(layers)):
    px = layers[j][i]
    if px == '2':
      continue
    else:
      out.append(px if px == '1' else '.')
      break
print(out)

for i in range(height):
  ch, out = chunk(out, width)
  print(''.join(ch))
