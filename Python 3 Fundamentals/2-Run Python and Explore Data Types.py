# EXERCISE 1
# EXERCISE 1
# EXERCISE 1
def greeting():
  hello="Hello"
  name= input("What is your name?\n")
  greeting =hello+" "+name
  print(greeting)


# EXERCISE 2
# EXERCISE 2
# EXERCISE 2
def taxCalculator():
  cost = float(input("Add total of puchase. Example 399.90\n"))
  tax = float(input("Add tax percentage as. Example 4.5\n"))
  total = cost + (cost*tax/100)
  print("Total to pay:$",total, sep="")


# EXERCISE 3
# EXERCISE 3
# EXERCISE 3
def ageCalculator():
  age = int(input("How old are you?\n"))
  decades = age//10
  years = age%10
  print("You are",decades,"decades and",years,"years old")


