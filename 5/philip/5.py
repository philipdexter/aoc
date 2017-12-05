import sys

arr = list(map(int, sys.stdin.read().strip().split('\n')))
l = len(arr)
idx = 0
steps = 0
while True:
    if idx < 0 or idx >= l:
        print(steps)
        exit(0)
    offset = arr[idx]
    if offset >= 3: arr[idx] -= 1
    else:           arr[idx] += 1
    idx += offset
    steps += 1
