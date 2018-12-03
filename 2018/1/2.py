freqs = set()
cfreq = 0
with open('1') as f:
  xs = list(map(int, f))
while True:
  for x in xs:
    if cfreq in freqs:
      print(cfreq)
      exit(0)
    freqs.add(cfreq)
    cfreq += x
