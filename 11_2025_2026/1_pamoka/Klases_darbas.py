"""
a = 9
b = 7.5
c = True
d = ""
e = None
f = 'Martynas'

print(a, end=" ")
print(type(a), id(a))

print(b, end=" ")
print(type(b), id(b))

print(c, end=" ")
print(type(c), id(c))

print(d, end=" ")
print(type(d), id(d))

print(e, end=" ")
print(type(e), id(e))

print(f, end=" ")
print(type(f), id(f))
"""

"""
a = 5

print(a, id(a))
a=6
print(a, id(a))

b=True
print(b, id(b))

b=False
print(b, id(b))
"""
"""
a = input("Įveskite skaičių")


if a.isdigit():
    a=int(a)
    print(a, type(a))
else:
    print("Įvestas ne skaičius")

"""

while True:
    vardas = input("Įveskite vardą\n")
    if vardas.isalpha():
        break
    print("Įvedėte ne raides")
print(vardas.capitalize())
