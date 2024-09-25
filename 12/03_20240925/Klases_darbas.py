a = [5, 6]

suma = a[0] + a[1]
print(f"{a[0]} + {a[1]} = {suma}")



def My_sum(x):
    x.append(x[0] + x[1])
    return x

print(My_sum(a))

#Savarankiška užduotis
#Duotas sąrašas

sarasas = ["Markas", "Adam", "Dina", "Donis", "Danieliai", "Airanas"]

#Parašykite funkciją kuri nuskaitytų sąrašą ir grąžintų elementus surušiuotus pagal abėcėlę
