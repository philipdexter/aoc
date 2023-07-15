
with open('input.txt') as f:
  line = f.read().strip()

for i in range(len(line)):
  fourteen = line[i:i+14]
  if len(set(fourteen)) == 14:
    print(i+14)
    break
