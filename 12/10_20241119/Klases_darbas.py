class TurtleCat(object):

    def __init__(self, name, fur, dry, shell=False, number_of_feet=4, tail=True):
        self.name=name
        self.fur=fur
        self.dry=dry
        self.shell=shell
        self.number_of_feet=number_of_feet
        self.tail=tail



    def voice(self):
        print("Roar")

    def swim(self):
        self.dry = False
        print(f"{self.name} is wet")

TurtleCat_1 = TurtleCat("Pranas", True, True, number_of_feet=7)

print(f"TurtleCat_1.name = {TurtleCat_1.name}")
print(f"TurtleCat_1.fur = {TurtleCat_1.fur}")
print(f"TurtleCat_1.dry = {TurtleCat_1.dry}")
print(f"TurtleCat_1.shell = {TurtleCat_1.shell}")
print(f"TurtleCat_1.number_of_feet = {TurtleCat_1.number_of_feet}")
print(f"TurtleCat_1.tail = {TurtleCat_1.tail}")

print("*"*80)
TurtleCat_1.swim()
print(f"TurtleCat_1.dry = {TurtleCat_1.dry}")
TurtleCat_1.voice()


TurtleCat_1.belekas = None

print(TurtleCat_1.belekas)
