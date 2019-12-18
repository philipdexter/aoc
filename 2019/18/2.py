
with open('2.txt') as f:
  input = f.readlines()

input = [line.strip() for line in input]

# input = [
#   '#######',
#   '#a.#Cd#',
#   '##@#@##',
#   '#######',
#   '##@#@##',
#   '#cB#Ab#',
#   '#######',
# ]

# input = [
#   '###############',
#   '#d.ABC.#.....a#',
#   '######@#@######',
#   '###############',
#   '######@#@######',
#   '#b.....#.....c#',
#   '###############',
# ]

# input = [
#   '#############',
#   '#DcBa.#.GhKl#',
#   '#.###@#@#I###',
#   '#e#d#####j#k#',
#   '###C#@#@###J#',
#   '#fEbA.#.FgHi#',
#   '#############',
# ]

# input = [
#   '#############',
#   '#g#f.D#..h#l#',
#   '#F###e#E###.#',
#   '#dCba@#@BcIJ#',
#   '#############',
#   '#nK.L@#@G...#',
#   '#M###N#H###.#',
#   '#o#m..#i#jk.#',
#   '#############',
# ]

poss = []
items = {}
for y in range(len(input)):
  for x in range(len(input[y])):
    if input[y][x] == '@':
      poss.append((x, y))
    items[(x, y)] = input[y][x]

def is_door(c):
  return c >= 'A' and c <= 'Z'

def is_key(c):
  return c >= 'a' and c <= 'z'

def dirs_of(p):
  return [(p[0], p[1] + 1),
          (p[0], p[1] - 1),
          (p[0] + 1, p[1]),
          (p[0] - 1, p[1]),]

keys = {}
for k in items:
  if is_key(items[k]):
    keys[items[k]] = k

def steps_to_locks(items, start, end):

  STACK = [(start, end, 0, [], [])]

  res = []

  while STACK:
    start, end, total_steps, locks, been = STACK.pop()

    if start == end:
      res.append((locks, total_steps))
      continue

    i = items.get(start)
    if is_door(i):
      locks = locks + [i.lower()]
    elif not is_key(i):
      if i not in ['.', '@']:
        continue

    been_now = been + [start]
    for d in dirs_of(start):
      if d not in been:
        if items.get(d) != '#':
          STACK.append((d, end, total_steps+1, locks, been_now))

  return res

dist_locks = {}
for i, pos in enumerate(poss):
  for end in keys:
    stl = steps_to_locks(items, pos, keys[end])
    if stl:
      dist_locks[('start' + str(i), end)] = stl
for start in keys:
  for end in keys:
    if start == end:
      continue
    stl = steps_to_locks(items, keys[start], keys[end])
    if stl:
      dist_locks[(start, end)] = stl

def can_access(start, unlocked):
  return [(path[1], way[1])
          for path, ways in dist_locks.items()
          if path[0] == start
          for way in ways
          if all([r in unlocked for r in way[0]])]

def but_with(starts, i, k):
  return starts[0:i] + (k,) + starts[i+1:]
CACHE = {}
def step(starts, unlocked):

  state_hash = (str(starts), str(sorted(unlocked)))
  if state_hash in CACHE:
    return CACHE[state_hash]

  options = []
  for start_index in range(len(starts)):
    start = starts[start_index]
    ca = [(k, s) for k, s in can_access(start, unlocked) if k not in unlocked]
    for k, s in ca:
      options.append(s + step(but_with(starts, start_index, k), unlocked + [k]))

  res = min(options) if options else 0
  CACHE[state_hash] = res
  return res

print(step(('start0', 'start1', 'start2', 'start3'), []))
