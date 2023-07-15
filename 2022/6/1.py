
with open('input.txt') as f:
  line = f.read().strip()

for i in range(len(line)):
  four = line[i:i+4]
  if len(set(four)) == 4:
    print(i+4)
    break
