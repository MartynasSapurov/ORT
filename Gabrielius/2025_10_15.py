#Pirmasis sekos narys x, o vis kiti generuojami pagal taisyklę:
#jei dabartinis narys x yra lyginis, tai sekantis narys bus x/2, prie6ingu atveju bus 3x+1
#Parašykite programą kuri genruotų seką kol bus gautas 1
"""
x = int(input("Enter a number: "))
print(x, end=", ")
while x > 1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
    print(x, end=", ")
"""
"""
x = int(input("Enter a number: "))
print(x, end=", ")

while x > 1:
    x = x // 2 if x % 2 == 0 else 3 * x + 1
    print(x, end=", ")
"""
#Nurodytas pradinis aukštis "a". Žinomas aukščių pasikeitimų kiekis "n" ir visi aukščio pokyčiai.
#Sukurkite programą, kuri išvestų galutinį aukštį bei skirtumą tarp galutinio ir pradinio aukščio "skirtumas"
"""
a, n = map(int, input("Įveskite pradinį aukštį ir pokyčių kiekį: ").split())

pokyciai = list(map(int, input("Įveskite pokyčius: ").split()[0:n]))

pradine = a

for item in pokyciai:
    a += item

print(f"{a}, skirtumas {pradine - a}")
"""
#Remdamiesi pirminiu pavyzdžiu parašykite programą, kuri atspausdintų pateiktą trikampį

