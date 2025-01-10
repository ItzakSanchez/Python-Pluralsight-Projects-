class Robot:
  def __init__(self, name):
    self.name = name
    self.position = [0,0]
    print("My name is:", name)
  
  def eat(self):
    print("I am hungry")
  
  def walk(self, x):
    self.position[0] = self.position[0]+x
    print("New position:",self.position)

class DogRobot(Robot):
  def makeNoise(self):
    print("Woof woof!")

  def eat(self):
    super().eat()
    print("I like bacon!")

def main():
  myDogRobot = DogRobot("Firulais")
  myDogRobot.walk(10)
  myDogRobot.makeNoise()
  myDogRobot.eat()

main()