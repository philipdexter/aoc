
lines = open('input.txt').read().strip().split('\n')

def valid(line):
  mins = dict()

  _, game = line.split(':')

  for pulls in game.split(';'):
    for pull in pulls.split(','):
      num, color = pull.strip().split(' ')
      num = int(num)
      if color not in mins:
        mins[color] = num
      elif num > mins[color]:
        mins[color] = num

  return mins['red'] * mins['blue'] * mins['green']

print(sum(map(valid, lines)))
