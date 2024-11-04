class Dog():

    #name = None
    #number_og_feet = 4
    #tail = True

    def __init__(self, name, number_og_feet, tail=True):
        self.name = name
        self.number_og_feet = number_og_feet
        self.tail = tail

    def say(self):
        print("Woof")

    def go(self):
        for item in range(1, self.number_og_feet+1):
            print(f"Step on {item} foot")

dog_1 = Dog("Lucky")

dog_1.say()

#dog_1.name = "Lucky"

print(f"dog_1.name = {dog_1.name}")
print(f"dog_1.number_og_feet = {dog_1.number_og_feet}")
print(f"dog_1.tail = {dog_1.tail}")

dog_1.go()
dog_1.number_og_feet = 3

print("*"*80)
dog_1.go()
