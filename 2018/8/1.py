
import sys

ds = ''.join(list(sys.stdin)).split()
print(ds)

metadatas = []

def read_node(ds):
  global metadatas
  nc, nm, *rest = ds
  nc = int(nc)
  nm = int(nm)
  for i in range(nc):
    rest = read_node(rest)
  metadata = rest[:nm]
  metadatas += list(map(int, metadata))
  return rest[nm:]

read_node(ds)

print(sum(metadatas))
