
import sys

class Marble:
  def __init__(self, number, counter, clockwise):
    self.number = number
    self.counter = counter
    self.clockwise = clockwise

class Circle:
  def __init__(self, marble):
    self.current = marble

  def counter(self):
    self.current = self.current.counter

  def clockwise(self):
    self.current = self.current.clockwise

  def insert_clockwise(self, m):
    m.clockwise = self.current.clockwise
    m.counter = self.current
    self.current.clockwise.counter = m
    self.current.clockwise = m

  def remove_counter(self):
    self.current.counter = self.current.counter.counter
    self.current.counter.clockwise = self.current


players = dict([(player + 1, 0) for player in range(int(sys.argv[1]))])
end_marble = int(sys.argv[2])

zero = Marble(0, None, None)
zero.counter = zero
zero.clockwise = zero
circle = Circle(zero)

def print_circle():
  current = zero
  if current == circle.current:
    print(f'({current.number}) ', end='')
  else:
    print(f'{current.number} ', end='')
  current = current.clockwise
  while current != zero:
    if current == circle.current:
      print(f'({current.number}) ', end='')
    else:
      print(f'{current.number} ', end='')
    current = current.clockwise
  print()

for m in range(end_marble):
  current_player = ((m+1) % len(players))
  if current_player == 0:
    current_player = len(players)
  # print(f'[{current_player}] ', end='')
  if (m+1) % 23 == 0:
    players[current_player] += m+1
    for i in range(6):
      circle.counter()
    players[current_player] += circle.current.counter.number
    circle.remove_counter()
  else:
    circle.clockwise()
    circle.insert_clockwise(Marble(m+1, None, None))
    circle.clockwise()
  # print_circle()
print(players)
winner = max(players.values())
print(winner)
