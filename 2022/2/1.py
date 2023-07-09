
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

def score(other: str, you: str) -> int:
  return score_choice(you) + score_winner(other, you)

print(sum([score(other, you)
           for line in lines
           if (split := line.split())
           if (other := split[0])
           if (you := split[1])]))
