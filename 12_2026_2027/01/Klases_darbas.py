class Dog(object):
    number_of_feet = 4
    tail = True
    name = "Spot"

    def say(self):
        print("Woof")
    
    def go(self):
        for item in range(1, self.number_of_feet+1):
            print(f"Step om {item} foot")


dog_1 = Dog()

dog_1.name = "Nano"
print(dog_1.name)

dog_2 = Dog()

print(dog_2.name)
print("*"*50)

dog_1.go()

***
Savarnkiškai sukurkite objektą automobilis, jisturi mokėti atlikti ne mažiau, nei 4 skirtingus veiksmus ir turėti nemažiau, nei 8 atribuus. Sukurkite bent 4 šios klasės objektus
***
