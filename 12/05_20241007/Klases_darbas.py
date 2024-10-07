my_list = [1, 4, 52, 69, 30, 3]

"""
for i in range(len(my_list)-1):
    if my_list[i] > my_list[i+1]:
        temp = my_list[i+1]
        my_list[i+1] = my_list[i]
        my_list[i] = temp
"""
"""
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
"""
"""
swapped = True
while True:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True
    if not swapped :
        break
print(my_list)
"""

#PAsitelkę sąrašų generatorių užpildykite sąrašą my_list 100 atsitiktinių sveikųjų skaičių verčių nuo 1 iki 999
#Rūšiavimo algoritmą (buble sort) įkelkite į atskirą funkciją kuri prrimtu nerūšiuotą sąrašą, o grąžintų surūšiuotą
#Pasitelkę biblioteką time palyginkite jūsų sukurto algoritmo ir sorted funkcijų trukmes
