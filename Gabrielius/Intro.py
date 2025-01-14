"""
Duoti du skaičiai a ir b. Parašykite programą, kuri rastų šių skaičių pirmųjų skaitmenų sumą
Pasitikrinkite. Jei a = 60203, o b = 432, tai turi būti išvesta: duotųjų skaičių pirmųjų skaitmenų suma yra 10
"""
"""
a = int(input("Įveskite pirmąjį skaičių\n"))
b = int(input("Įveskite antrąjį skaičių\n"))

while a > 10:
    a = int(a/10)

while b > 10:
    b = int(b/10)
"""
a = int(input("Įveskite pirmąjį skaičių\n")[0])
b = int(input("Įveskite antrąjį skaičių\n")[0])

print(f"Skaičių a ir b suma lygi {a+b}")
