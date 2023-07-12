
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

stacks = [
  'NVCS',
  'SNHJMZ',
  'DNJGTCM',
  'MRWJFDT',
  'HFP',
  'JHZTC',
  'ZLSFQRPD',
  'WPFDHLSC',
  'ZGNFPMSD',
]

for line in lines:
  move, from_, to = [int(x) for x in line.split(',')]
  from_ -= 1
  to -= 1
  moving = stacks[from_][:move]
  stacks[from_] = stacks[from_][move:]
  stacks[to] = moving + stacks[to]
print(''.join([x[0] for x in stacks]))
