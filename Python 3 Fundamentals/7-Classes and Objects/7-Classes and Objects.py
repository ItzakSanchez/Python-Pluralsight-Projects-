class RobotDog:

  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print("Woof Woof!")

dog1 = RobotDog("Firulais", "Chihuahua")

print(dog1.name)
print(dog1.breed)
dog1.bark()