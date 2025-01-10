
#EXERCISE 1
#EXERCISE 1
#EXERCISE 1
def usingLists():
  acronyms = ["LOL", "IDK", "TBH", "IMO", "SMH"]
  acronyms.append("BFN")
  acronyms.remove("IMO")

  if not "BRB" in acronyms:
    acronyms.append("BRB")
  print(acronyms)
  print(acronyms[0])
  print(acronyms[-1])
  print("---")

  for acronym in acronyms:
    print(acronym)


#EXERCISE 2
#EXERCISE 2
#EXERCISE 2
def sumExpences():
  expences = []
  expence = 0
  print("Add expences to get Total. Send empty expence to finish inputs and get the total")
  while True:
    expence = input("Add expence: ")
    if expence == "":
      break
    expence = float(expence)
    expences.append(expence)

  total = sum(expences)

  # total=0
  # for expence in expences:
  #   total = total+expence

  print("Total: $",total, sep="")


#EXERCISE 3
#EXERCISE 3
#EXERCISE 3
def compoundInterestCalculator():
  initialDeposit = float(input("Enter yout intial deposit. ex:30000\n"))
  interest = float(input("Set the interest percentage rate. ex:9.2\n"))
  periods = int(input("Set the number of years of invesment. ex:4\n"))
  recurringDeposit = float(input("Set value of recurring deposit ex:1000\n"))

  total = initialDeposit
  accruedInterest=0
  totalRecurrungDeposit=0
  
  for i in range(periods):
    currentValue = total+ recurringDeposit
    
    tempInterest = currentValue*(interest/100)
    currentValue = total+recurringDeposit
    
    totalRecurrungDeposit += recurringDeposit #GLOBAL
    accruedInterest += tempInterest #GLOBAL

    total = currentValue+tempInterest
    
  print("Total value at end of investment:$",total)
  print("Total Accrued Interest:$",accruedInterest)
  print("Total Recurrung Deposit:$",totalRecurrungDeposit)

#EXERCISE 4
#EXERCISE 4
#EXERCISE 4
def BMICalculator():
  weight = float(input("Weight (Kg): "))
  height = float(input("Height (Cm): "))/100

  bmi = weight/(height**2)
  print("Your BMI is:",bmi)
