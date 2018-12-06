
import sys
from collections import defaultdict

times = defaultdict(list)

current_guard = None
fell_asleep = None
fell_asleep_date = None
is_asleep = False
def parse(line):
  global is_asleep, fell_asleep, fell_asleep_date, current_guard
  parts = line.rstrip().split()
  time = parts[1].rstrip(']')
  if parts[2] == 'Guard':
    if is_asleep:
      is_asleep = False
      process_asleep(current_guard, fell_asleep, time)
    current_guard = int(parts[3].lstrip('#'))
  elif parts[2] == 'wakes':
    if is_asleep == False:
      fell_asleep = '0:0'
    is_asleep = False
    process_asleep(current_guard, fell_asleep, time)
  elif parts[2] == 'falls':
    if is_asleep and fell_asleep_date != parts[0]:
      process_asleep(current_guard, fell_asleep, '0:60')
    is_asleep = True
    fell_asleep_date = parts[0]
    fell_asleep = time
  else:
    print(f'bad line {parts}')
    exit(1)

def parse_time(time):
  return int(time.split(':')[1])

def process_asleep(guard, start, end):
  start = parse_time(start)
  end = parse_time(end)
  for t in range(start, min(end,60)):
    times[t].append(guard)

def stime(line):
  parts = line.split()
  return f'{parts[0].lstrip("[")}{parts[1].rstrip("]")}'

entries = list(sys.stdin)
print(sorted(entries, key=stime))
list(map(parse, sorted(entries, key=stime)))
print(times)

guards_to_time = defaultdict(lambda: 0)
for t in times:
  for g in times[t]:
    guards_to_time[g] += 1
the_guard = max(guards_to_time.items(), key=lambda x: x[1])[0]
print(max(guards_to_time.items(), key=lambda x: x[1]))

most_time_guard = -1
most = 0
for t in times:
  gt = times[t].count(the_guard)
  if gt >= most:
    most = gt
    most_time_guard = t
print(most_time_guard)
