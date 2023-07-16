
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

path = []
disk = {}
dirs = {}

def set_(name: str, size: int):
  global path, disk
  d = disk
  build_path = ''
  for p in path:
    build_path += p + '/'
    if build_path not in dirs:
      dirs[build_path] = 0
    dirs[build_path] += size
    if p in d:
      d = d[p]
    else:
      d[p] = {}
      d = d[p]
  d[name] = size

for i in range(len(lines)):
  line = lines[i]
  if line.startswith('$'):
    if line.startswith('$ cd'):
      name = line.split(' cd ')[1]
      if name == '..':
        path.pop()
      else:
        path.append(name)
    elif line.startswith('$ ls'):
      ...
      while True:
        i += 1
        if i + 1 > len(lines):
          break
        line = lines[i]
        if line.startswith('$'):
          break
        if line.startswith('dir'):
          ...
        else:
          size, name = line.split()
          set_(name, int(size))
    else:
      raise Exception(f'bad cmd {line}')

total = 0
for d in dirs:
  if dirs[d] <= 100000:
    total += dirs[d]

left = 70000000 - dirs['//']
want = 30000000 - left
candidates = [(k, v) for k, v in dirs.items() if v > want]
print(min(candidates, key=lambda x: x[1]))
