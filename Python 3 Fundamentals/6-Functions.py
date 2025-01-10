import random

#EXERCISE 1
#EXERCISE 1
#EXERCISE 1
def rollDice():
  return [random.randint(1,6),random.randint(1,6)]

def main():
  player1 = input("Enter player 1's name\n")
  player2 = input("Enter player 2's name\n")

  result1 = rollDice()
  result2 = rollDice()

  print(player1, "rolled",result1,"Total:",sum(result1))
  print(player2, "rolled",result2,"Total:",sum(result2))

  if result1>result2:
    print(player1,"wins!")
  elif result2>result1:
    print(player2,"wins!")
  else:
    print("Tie!")

main()