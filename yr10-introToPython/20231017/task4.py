import statistics
from random import randint
rolls: list[int] = []
while True:
  action: str = input("Roll (r) or Quit (Q)")
  if action == "r":
    tempRand: int = randint(1,6)
    rolls.append(tempRand)
    print(tempRand)
  else:
    print(f"Average roll {statistics.mode(rolls)}")
    break
