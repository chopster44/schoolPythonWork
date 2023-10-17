from random import randint
print("Welcome to rock paper scissors")

playerScore: int = 0
computerScore: int = 0

while True:
  print(f"Current score: Player {playerScore} - Computer {computerScore}")
  action: int = int(input("Rock (1), Paper (2), Scissors (3), Quit (4)"))
  if action == 4:
    break
  computerAction: int = randint(1,3)
  match computerAction:
    case 1:
      print("Computer plays Rock")
    case 2:
      print("Computer plays Paper")
    case 3:
      print("Computer plays Scissors")  
    case _ :
      pass


  
  if action == 1:
    if computerAction == 2:
      print("Computer wins")
      computerScore +=1
    else:
      print("You win")
      playerScore += 1
  elif action == 2:
    if computerAction == 3:
      print("Computer wins")
      computerScore +=1
    else:
      print("You win")
      playerScore += 1

  elif action == 3:
    if computerAction == 1:
      print("Computer wins")
      computerScore +=1
    else:
      print("You win")
      playerScore += 1
  else:
    print("Invalid action")
