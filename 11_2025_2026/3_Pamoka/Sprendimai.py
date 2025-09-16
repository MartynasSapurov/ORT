"""
1 Užduotis


kiekis = int(input("Įveskite sekos ilgį\n"))
seka = []

for _ in range(kiekis):
    seka.append(int(input("Įveskite skaičių ")))

print(seka[0])
"""

"""
2 Užduotis

kiekis = int(input("Įveskite sekos ilgį\n"))
seka = []

for _ in range(kiekis):
    seka.append(int(input("Įveskite skaičių ")))

print(len(seka))
print(seka[0]+seka[-1])
"""

"""
3 Užduotis

kiekis = int(input("Įveskite sekos ilgį\n"))
seka = []

for _ in range(kiekis):
    seka.append(int(input("Įveskite skaičių ")))
suma = 0

for item in seka:
    suma += item

#for _ in range(kiekis):
#    suma += seka[_]



print(suma)
"""

"""
4 Užduotis

kiekis = int(input("Įveskite sekos ilgį\n"))
seka = []

for _ in range(kiekis):
    seka.append(int(input("Įveskite skaičių ")))

suma = 0

for item in seka:
    suma += item

print(suma/kiekis)

"""
"""
5 Užduotis


kiekis = int(input("Įveskite sekos ilgį\n"))
seka = []

for _ in range(kiekis):
    seka.append(int(input("Įveskite skaičių ")))

for i in range(1, kiekis-1):
    average= (seka[i-1]+seka[i]+seka[i+1])/3
    print(average)
"""
