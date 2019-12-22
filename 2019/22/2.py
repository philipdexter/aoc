
with open('1.txt') as f:
  input = f.readlines()

input = [line.strip() for line in input]

ll = 119315717514047

def process(s):
  parts = s.split()
  if parts == ['deal', 'into', 'new', 'stack']:
    return ('rev', None)
  if parts[:-1] == ['deal', 'with', 'increment']:
    return ('inc', int(parts[-1]))
  return ('cut', int(parts[-1]))

def doit(i):
  n = 135
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 38
  i = (i * n) % ll

  i = ll - i - 1

  n = 29
  i = (i * n) % ll

  n = 120
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 30
  i = (i * n) % ll

  i = ll - i - 1

  n = 7198
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  i = ll - i - 1

  n = 59
  i = (i * n) % ll

  n = 8217
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 75
  i = (i * n) % ll

  n = 4868
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 29
  i = (i * n) % ll

  n = 4871
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 2
  i = (i * n) % ll

  i = ll - i - 1

  n = 54
  i = (i * n) % ll

  n = 777
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 40
  i = (i * n) % ll

  n = 8611
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 3
  i = (i * n) % ll

  n = 5726
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 57
  i = (i * n) % ll

  i = ll - i - 1

  n = 41
  i = (i * n) % ll

  i = ll - i - 1

  n = 5027
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 12
  i = (i * n) % ll

  n = 5883
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 45
  i = (i * n) % ll

  n = 9989
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 14
  i = (i * n) % ll

  n = 6535
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 18
  i = (i * n) % ll

  n = 5544
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 29
  i = (i * n) % ll

  i = ll - i - 1

  n = 64
  i = (i * n) % ll

  i = ll - i - 1

  n = 41
  i = (i * n) % ll

  i = ll - i - 1

  n = 6
  i = (i * n) % ll

  n = 4752
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 8
  i = (i * n) % ll

  i = ll - i - 1

  n = 26
  i = (i * n) % ll

  n = 6635
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 10
  i = (i * n) % ll

  i = ll - i - 1

  n = 3830
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 48
  i = (i * n) % ll

  i = ll - i - 1

  n = 39
  i = (i * n) % ll

  n = 4768
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 65
  i = (i * n) % ll

  i = ll - i - 1

  n = 5417
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 15
  i = (i * n) % ll

  n = 4647
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  i = ll - i - 1

  n = 3596
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 17
  i = (i * n) % ll

  n = 3771
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 50
  i = (i * n) % ll

  n = 1682
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  i = ll - i - 1

  n = 20
  i = (i * n) % ll

  i = ll - i - 1

  n = 22
  i = (i * n) % ll

  i = ll - i - 1

  n = 3
  i = (i * n) % ll

  n = 8780
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 52
  i = (i * n) % ll

  n = 7478
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 9
  i = (i * n) % ll

  n = 8313
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  i = ll - i - 1

  n = 742
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 19
  i = (i * n) % ll

  n = 9982
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  i = ll - i - 1

  n = 68
  i = (i * n) % ll

  n = 9997
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 23
  i = (i * n) % ll

  n = 240
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 54
  i = (i * n) % ll

  n = 7643
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  i = ll - i - 1

  n = 6
  i = (i * n) % ll

  n = 3493
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  n = 74
  i = (i * n) % ll

  i = ll - i - 1

  n = 75
  i = (i * n) % ll

  i = ll - i - 1

  n = 40
  i = (i * n) % ll

  n = 596
  if i < n:
    i = ll - n + i
  else:
    i = i - n

  n = 6
  i = (i * n) % ll

  n = 4957
  if i < ll - n:
    i = i + n
  else:
    i = i - (ll - n)

  i = ll - i - 1

  return i

steps = [process(line) for line in input]

def where(i):
  for step in steps:
    if step[0] == 'rev':
      i = ll - i - 1
    elif step[0] == 'cut':
      n = step[1]
      if n > 0:
        if i < n:
          i = ll - n + i
        else:
          i = i - n
      else:
        n = abs(n)
        if i < ll - n:
          i = i + n
        else:
          i = i - (ll - n)
    else:
      n = step[1]
      i = (i * n) % ll
  return i

# def backwards(i):
#   for step in steps:
#     if step[0] == 'rev':
#       i = ll - i - 1
#     elif step[0] == 'cut':
#       n = step[1]
#       if i < n:
#         i = (-ll) + n - i
#       else:
#         i = i + n
#     else:
#       n = step[1]
#       i = (i * n) % ll
#   return i
