"""
Turime tris kintamuosius v, a ir b. Kintamasis v nurodo veiksmą (1 – sudėtis, 2 – daugyba, 3 – dalyba, 4 –
atimtis). Sukurkite 4 funkcijas sud, daug, dal, atim, kurios išvestų atlikto veiksmo rezultatą. Sukurkite funkciją
klaida, kuri išvestų pranešimą „blogas pasirinkimas“. Blogo pasirinkimo atveju vartotojas neturi įvesti a ir b
reikšmių.
"""
def sud(a, b):
    print(f"Sudėtis: {a+b}")

def daug(a, b):
    print(a*b)

def atim(a, b):
    print(a - b)

def dal(a, b):
    if b != 0:
        print(a/b)
    else:
        print("Dalyba iš nulio")

def klaida():
    print("blogas pasirinkimas")

v, a, b = map(int, input("Įveskite veiksmus\n").split())


if v == 1:
    sud(a, b)
elif v == 2:
    atim(a, b)
elif v == 3:
    daug(a, b)
elif v == 4:
    dal(a, b)
else:
    klaida()
