"""
def maksim():
    print("Maksim")

def kvadratas(x):
    return x*x

def sandauga(x, y=3):
    return x*y

def dalyba(x, y):
    return x/y

sk1 = int(input())
sk2 = int(input())

print(kvadratas(sk1))

print(sandauga(sk1, sk2))

print(dalyba(sk1, y = sk2))

#Parašykite funkcija, kuri nuskaitytų skaičių įvesta klaviatūra ir jeigu tai skaačius atspausdintų "Number",
#jeigu ne, "Not number", funkcijos pavadinimas tikrinimas()
"""
"""
def tikrinimas():

    if input().isdigit():
        return "Number"
    else:
        return "Not nuber"

print(tikrinimas())
"""

def dviem_daugiau(x, y):
    x+=2
    y+=2
    return x, y

a, b = dviem_daugiau(1, 2)
print(a, b)

#Parašykite programą kuri prašytų jūsų įvesti skaičių tol kol bus įvestas skaitmuo, jeigu įvedamas tekstas
#prašo įvesti skaičių dar kartą, naudokite vieną funkciją skaičiaus įvcedimui ir tikrinimui

