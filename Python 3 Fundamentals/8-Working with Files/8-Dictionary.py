#EXERCISE 1
#EXERCISE 1
#EXERCISE 1
def remainder_division(a,b):
  if b ==0:
    raise Exception()
  division = a//b
  reminder= a%b

  print(a,"/",b,"is",division,"remainder",reminder)

#EXERCISE 2
#EXERCISE 2
#EXERCISE 2
def findAcronym():

  acronym = input("Enter acronym to find for:\n").lower()

  found = False
  try:
    file = open(r"C:\Users\edgar\Desktop\Python\Python 3 Fundamentals\8-Working with Files\dictionary.txt", "r")
    for line in file:
      line= line.lower()
      if acronym in line:
        found = True
        print(line)
        break   
    file.close()
  except FileNotFoundError as ex:
    print("Fie not found.")
    return
  
  if not found:
    print("Acronym not found")

def writeAcronym():
  acronym = input("What acronym do you want to add? e.g. IDK\n") 
  meaning = input("What is the definition?\n")
  try:
    file = open(r"C:\Users\edgar\Desktop\Python\Python 3 Fundamentals\8-Working with Files\dictionary.txt", "a")
    file.write("\n"+acronym+" - "+meaning)
    file.close()
  except FileNotFoundError as ex:
    print("Fie not found.")

def main():
  choice = input("Do you want to find (f) or add (a) an acronym?")
  choice = choice.lower()
  if choice =="f":
    findAcronym()
  elif choice=="a":
    writeAcronym()


main()