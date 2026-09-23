class Dog(object):
    number_of_feet = 4
    tail = True
    name = "Spot"

    def say(self):
        print("Woof")
    
    def go(self):
        for item in range(1, self.number_of_feet+1):
            print(f"Step om {item} foot")

    def add_foot(self, amount):
        self.number_of_feet += amount

dog_1 = Dog()

dog_1.name = "Nano"
print(dog_1.name)

dog_2 = Dog()

print(dog_2.name)
print("*"*50)

dog_1.go()
dog_1.add_foot(4)

print(dog_1.number_of_feet)

"""
class Dog(object):
  
    def __init__(self, number_of_feet=4, tail = True, name = "Spot"):
        self.number_of_feet = number_of_feet
        self.tail = tail
        self.name = name

    def say(self):
        print("Woof")
    
    def go(self):
        for item in range(1, self.number_of_feet+1):
            print(f"Step om {item} foot")

    def add_foot(self, amount):
        self.number_of_feet += amount

    def add_atribute(self):
        self.breed = "Terjeras"

dog_1 = Dog(3, False, "Pies")
dog_2 = Dog()

print(dog_1.number_of_feet, dog_1.tail, dog_1.name)
"""
