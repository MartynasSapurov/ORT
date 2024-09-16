#Parašykite lambda funkcija kuri nuskaitytų duotą sąrašą ir jei pirmoji žodžio sąraše raide = 'a' arba 'A' grąžintų
#paskutinius tris simbolius didžiosiomis raidėmis, jei pirmoji radė nelygi 'a' arba 'A' grąžintų pirus tris simbolius mažosiomis raidėmis.

my_list = ['Albert', 'bob', 'Robert', 'aliona', 'Algirdas', 'alicija', 'UZDUOTIS', 'piramSiS']
"""
def zodis(a):
    if a[0].lower() == 'a':
        return a[-3:].upper()
    else:
        return a[:3].lower()
"""

"""
def zodis(a):
    return a[-3:].upper() if a[0].lower() == 'a' else a[:3].lower()
"""

zodis = lambda a: a[-3:].upper() if a[0].lower() == 'a' else a[:3].lower()
"""
print(zodis(my_list[5]))

print((lambda a: a[-3:].upper() if a[0].lower() == 'a' else a[:3].lower())(my_list[5]))
"""

"""
my_new_list = []
for b in my_list:
    my_new_list.append(zodis(b))
"""

#my_new_list = [(lambda a: a[-3:].upper() if a[0].lower() == 'a' else a[:3].lower())(b) for b in my_list]

my_new_list = [zodis(b) for b in my_list]

print(my_list)
print(my_new_list)
print("*"*40)



sarasas = lambda c: [d[-3:].upper() if d[0].lower() == 'a' else d[:3].lower() for d in c]

"""
def sarasas(c):
 return [d[-3:].upper() if d[0].lower() == 'a' else d[:3].lower() for d in c]
"""
"""
    e = []
    for d in c:
        e.append(d[-3:].upper()) if d[0].lower() == 'a' else e.append(d[:3].lower())
    return e
"""
"""
        if d[0].lower() == 'a':
            e.append(d[-3:].upper())
        else:
            e.append(d[:3].lower())
"""

print(sarasas(my_list))
