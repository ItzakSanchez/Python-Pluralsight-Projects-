import random

# EXERCISE 1
# EXERCISE 1
# EXERCISE 1
def watherRecomendations():
  forecast = "rainy"
  if not forecast == "rainy":
    print("It is not raining")
  else:
    print("It's raining!")

  #Celcius
  temperature = 20
  if temperature<10:
    print("Its too cold. Stay inside")
  elif temperature>32:
    print("It's too hot. Stay inside")
  else:
    print("Have a nice day")

# EXERCISE 2
# EXERCISE 2
# EXERCISE 2
def rockPaperSissorsGame():
  computer_choize = random.choice(["rock", "paper", "sissors"])
  print("Let's play rock paper sissors.")
  user_choice = input("Your choice: ")

  print("Computer's choice:", computer_choize)
  if not (user_choice=="sissors" or user_choice=="paper" or user_choice=="rock"):
    print("Invalid choice. Choices: rock paper sissors")
  elif user_choice==computer_choize:
    print("Tie")
  elif user_choice=="rock" and computer_choize=="sissors":
    print("You win!")
  elif user_choice=="paper" and computer_choize=="rock":
    print("You win!")
  elif user_choice=="sissors" and computer_choize=="paper":
    print("You win!")
  else:
    print("You lose. Computer wins >:)")
  
# EXERCISE 3
# EXERCISE 3
# EXERCISE 3
def guessRollDice():
  roll = random.randint(1,6)
  user_guess = int(input("Can you guess the value of the dice 1-6\n"))

  if(user_guess == roll):
    print("Correct, dice value is:",roll)
  else:
    print("Wrong, dice value is:",roll)