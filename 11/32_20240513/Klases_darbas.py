#Duotas sąrašas sudarytas iš skirtingų tipų
#Taikydami map() funkciją parašykite programą kuri grąžintų sąrašą kuriame kiekvienas int tipo kintamasis būtų pakeistas į str tipą,
#visus kitų tipų elementus į sąrašą nekeisdamas. Duomenų pakeitimui map funkcijos viduje panaudokite lamda funkcija.

values = [1.33, 2, '3', 'forth', 'end', 99, 2.354, True, False, None]

pakeitimai = lambda a: str(a) if isinstance(a, int) else a


new_list = map(lambda a: str(a) if isinstance(a, int) else a, values)

for item in new_list:
        print(f"Value {item}, type {type(item)}")

"""
def pakeitimai (a):
    return str(a) if isinstance(a, int) else a

    if isinstance(a, int):
        return str(a)
    else:
        return a
"""



"""
for item in values:
        print(f"Value {item}, type {type(item)} ")

a = 1.0
b = 33

if isinstance(a, int):
    print("a is integer")

if isinstance(b, int):
    print("b is integer")

"""
