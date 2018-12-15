
from dataclasses import dataclass

@dataclass
class Cart:
  arrow: str
  pos: (int, int)
  turn: str

  def turn_me(self):
    ret = self.turn
    self.turn = {'left': 'straight',
                 'straight': 'right',
                 'right': 'left'}[self.turn]
    return ret

@dataclass
class Track:
  pos: (int, int)
  piece: str

  def next_pos(self, cart):
    arrow = cart.arrow
    if self.piece == '|':
      if arrow == 'V':
        cart.pos = shift(cart.pos, (0,1))
      elif arrow == '^':
        cart.pos = shift(cart.pos, (0,-1))
      else:
        raise Exception('bad case for |')
    elif self.piece == '-':
      if arrow == '>':
        cart.pos = shift(cart.pos, (1,0))
      elif arrow == '<':
        cart.pos = shift(cart.pos, (-1,0))
      else:
        raise Exception('bad case for -')
    elif self.piece == '/':
      if arrow == '^':
        cart.pos = shift(cart.pos, (1,0))
        cart.arrow = '>'
      elif arrow == '<':
        cart.pos = shift(cart.pos, (0,1))
        cart.arrow = 'V'
      elif arrow == 'V':
        cart.pos = shift(cart.pos, (-1,0))
        cart.arrow = '<'
      elif arrow == '>':
        cart.pos = shift(cart.pos, (0,-1))
        cart.arrow = '^'
      else:
        raise Exception('bad case for /')
    elif self.piece == '\\':
      if arrow == '^':
        cart.pos = shift(cart.pos, (-1,0))
        cart.arrow = '<'
      elif arrow == '<':
        cart.pos = shift(cart.pos, (0,-1))
        cart.arrow = '^'
      elif arrow == 'V':
        cart.pos = shift(cart.pos, (1,0))
        cart.arrow = '>'
      elif arrow == '>':
        cart.pos = shift(cart.pos, (0,1))
        cart.arrow = 'V'
      else:
        raise Exception('bad case for \\')
    elif self.piece == '+':
      turn = cart.turn_me()
      if arrow == '>':
        if turn == 'left':
          cart.pos = shift(cart.pos, (0,-1))
          cart.arrow = '^'
        elif turn == 'straight':
          cart.pos = shift(cart.pos, (1,0))
        elif turn == 'right':
          cart.pos = shift(cart.pos, (0,1))
          cart.arrow = 'V'
        else:
          raise Exception('bad case for + >')
      elif arrow == '<':
        if turn == 'left':
          cart.pos = shift(cart.pos, (0,1))
          cart.arrow = 'V'
        elif turn == 'straight':
          cart.pos = shift(cart.pos, (-1,0))
        elif turn == 'right':
          cart.pos = shift(cart.pos, (0,-1))
          cart.arrow = '^'
        else:
          raise Exception('bad case for + <')
      elif arrow == 'V':
        if turn == 'left':
          cart.pos = shift(cart.pos, (1,0))
          cart.arrow = '>'
        elif turn == 'right':
          cart.pos = shift(cart.pos, (-1,0))
          cart.arrow = '<'
        elif turn == 'straight':
          cart.pos = shift(cart.pos, (0,1))
        else:
          raise Exception('bad case for + V')
      elif arrow == '^':
        if turn == 'left':
          cart.pos = shift(cart.pos, (-1,0))
          cart.arrow = '<'
        elif turn == 'right':
          cart.pos = shift(cart.pos, (1,0))
          cart.arrow = '>'
        elif turn == 'straight':
          cart.pos = shift(cart.pos, (0,-1))
        else:
          raise Exception('bad case for + ^')
    else:
      raise Exception(f'no case match for {cart}')

def shift(pos, by):
  return (pos[0] + by[0], pos[1] + by[1])

grid = {}
carts = []

import sys
lines = list(sys.stdin)
max_x = len(lines[0])
max_y = len(lines)
for y in range(max_y):
  for x in range(max_x):
    c = lines[y][x]

    if c in ['V', '^', '<', '>']:
      carts.append(Cart(pos=(x,y), turn='left', arrow=c))

    if c in ['>', '<']:
      c = '-'
    elif c in ['^', 'V']:
      c = '|'

    if c in ['/', '\\', '-', '|', '+']:
      grid[(x,y)] = Track(pos=(x,y), piece=c)

def print_grid():
  cs = {cart.pos: cart.arrow for cart in carts}
  for y in range(max_y):
    for x in range(max_x):
      if cs.get((x,y)):
        print(cs[(x,y)], end='')
      else:
        to_print = grid.get((x,y))
        to_print = to_print.piece if to_print else ' '
        print(to_print, end='')
    print()

def step():
  for c in carts:
    grid[c.pos].next_pos(c)
  cart_positions = list(map(lambda c: c.pos, carts))
  if len(cart_positions) != len(set(cart_positions)):
    print(steps)
    from collections import Counter
    print([item for item, count in Counter(cart_positions).items() if count > 1])
    exit(0)

steps = 0
print_grid()
print('======')
while True:
  steps += 1
  step()
  print_grid()
  print('======')
