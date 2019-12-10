import operator

with open('input') as f:
    dirs = f.read().strip().split(',')

ds={
    's': (-1,1,0),
    'sw': (-1,0,1),
    'nw': (0,-1,1),
    'n': (1,-1,0),
    'ne': (1,0,-1),
    'se': (0,1,-1),
}

position = (0,0,0)

def distance(a, b):
    x,y,z = tuple(map(operator.sub, a, b))
    return (abs(x) + abs(y) + abs(z)) // 2

diff = 0
for d in dirs:
    position = tuple(map(operator.add, position, ds[d]))
    diff = max(diff, distance((0,0,0), position))

print(diff)
print(distance((0,0,0), position))
