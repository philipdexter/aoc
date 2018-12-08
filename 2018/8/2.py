
import sys

ds = ''.join(list(sys.stdin)).split()
print(ds)

def read_node(ds):
  nc, nm, *rest = ds
  nc = int(nc)
  nm = int(nm)
  child_vals = []
  for i in range(nc):
    rest, cval = read_node(rest)
    child_vals.append(cval)
  metadata = list(map(int, rest[:nm]))
  if nc == 0:
    val = sum(metadata)
  else:
    val = 0
    print(child_vals)
    for i in metadata:
      print('looking for ' + str(i))
      if i >= 1 and i < len(child_vals)+1:
        val += child_vals[i-1]
  print(val)

  return rest[nm:], val

print(read_node(ds))
