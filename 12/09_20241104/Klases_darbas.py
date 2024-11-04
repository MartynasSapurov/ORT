class Dog(object):

    def __init__(self, name, number_og_feet=4, tail=True):
        self.name = name
        self.number_og_feet = number_og_feet
        self.tail = tail

    def say(self):
        print("Woof")

    def go(self):
        for item in range(1, self.number_og_feet+1):
            print(f"Step on {item} foot")

    def add_atribute(self):
        self.breed = None

dog_1 = Dog("Lucky")
dog_1.breed = "Biewer"
#dog_1.my_init("Lucky")
dog_1.say()

print(type(dog_1.name))
print(type(dog_1.number_og_feet))


#dog_1.name = "Lucky"
print("*"*80)
print(f"dog_1.name = {dog_1.name}")
print(f"dog_1.number_og_feet = {dog_1.number_og_feet}")
print(f"dog_1.tail = {dog_1.tail}")
print(f"dog_1.breed = {dog_1.breed}")
print("*"*80)
dog_1.go()
dog_1.number_og_feet = 3

print("*"*80)
dog_1.go()
print("*"*80)
dog_2 = Dog("Rex", 4, False)
dog_2.add_atribute()
print(f"dog_2.name = {dog_2.name}")
print(f"dog_2.number_og_feet = {dog_2.number_og_feet}")
print(f"dog_2.tail = {dog_2.tail}")
print(f"dog_2.breed = {dog_2.breed}")
