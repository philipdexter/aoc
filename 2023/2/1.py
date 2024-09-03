
lines = open('input.txt').read().strip().split('\n')

max = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def valid(line):
  game_num, game = line.split(':')

  for pulls in game.split(';'):
    for pull in pulls.split(','):
      num, color = pull.strip().split(' ')
      if int(num) > max[color]:
        return 0

  return int(game_num)

print(sum(map(valid, lines)))
