
with open('input.txt') as f:
  lines = f.read().strip().split('\n')

def score_choice(choice: str) -> int:
  match choice:
    case 'X':
      return 1
    case 'Y':
      return 2
    case 'Z':
      return 3

def score_winner(other: str, you: str) -> int:
  if other == 'A' and you == 'X' or other == 'B' and you == 'Y' or other == 'C' and you == 'Z':
    return 3
  if other == 'A' and you == 'Y':
    return 6
  if other == 'B' and you == 'Z':
    return 6
  if other == 'C' and you == 'X':
    return 6
  return 0

def my_choice(other: str, outcome: str) -> str:
  match (other, outcome):
    case ('A', 'X'): return 'Z'
    case ('A', 'Y'): return 'X'
    case ('A', 'Z'): return 'Y'
    case ('B', 'X'): return 'X'
    case ('B', 'Y'): return 'Y'
    case ('B', 'Z'): return 'Z'
    case ('C', 'X'): return 'Y'
    case ('C', 'Y'): return 'Z'
    case ('C', 'Z'): return 'X'

def score(other: str, outcome: str) -> int:
  you = my_choice(other, outcome)
  return score_choice(you) + score_winner(other, you)

print(sum([score(other, you)
           for line in lines
           if (split := line.split())
           if (other := split[0])
           if (you := split[1])]))
