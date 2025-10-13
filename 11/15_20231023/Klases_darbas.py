#Sąrašų generatoriai
#Elementų indeksai sąrašuose
my_old_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
my_item = 2

for index, item in enumerate(my_old_tuple):
    if item == my_item:
        print(f"Skaičiaus {my_item} indeksas = {index}")

#Kitas būdas pasitelkiant kortežų metodus
print(f"Skaičiaus {my_item} indeksas = {my_old_tuple.index(my_item)}")

#If Else sakinio užrašymas viena eilute
#Standartine forma išrenkame didžiausę vertę
a = 2
b = 5

if a > b:
    max = a
else:
    max = b
print(max)

#Tą patį atliekame perrašę sąklygos sakinį viena eilute
max = a if a>b else b
print(max)

#Sąrašo generavimas pasitelkiant for ciklą
my_new_list = [] #Sukuriamas tuščias sąrašas

for i in range(20):
    my_new_list.append(i) #Sukuriame 20 naujų elementų
print(my_new_list)

#Kitas varinatas sąrašo sukūrimas paitelkiant sąrašų generatorius
my_new_list = [i for i in range(20)]
print(my_new_list)

#Sukuriame naują kortežą pasinaudoję esamu kortežu, bet visus elementus išrikiuojame atvirkščiai
my_new_tuple = tuple(item for item in my_old_tuple[::-1])
print(my_old_tuple)
print(my_new_tuple)

#Sukuriame naują kortežą pasinaudoję esamu kortežu, bet sukuriame tik lyginių verčių elementus
my_new_tuple = tuple(item for item in my_old_tuple if not(item % 2))
print(my_old_tuple)
print(my_new_tuple)

#Darbas su eilutėmis, atskiraime "," atskirtus elementus ir surašome į sąrašą jų skaitines vertes
my_string = "1,3,5,7,8,10,15,14"

my_string_list = []

for item in my_string.split(","):
    my_string_list.append(int(item))
print(my_string)
print(my_string_list)

#Verčių sąrašo sukūrimas pasitelkiant sąrašų generatorių
my_string_list = [int(item) for item in my_string.split(",")]
print(my_string)
print(my_string_list)

#my_string_tuple = tuple(item for item in my_string)

#darbas su žodynais
my_dict = {"Vienas": "One", "Du": "Two", "Trys": "Three", "Keturi": "Four", "Penki": "Five", "Sesi": "Six", "Septyni": "Seven", "Astuoni": "Eight", "Devyni": "Nine"}
my_dict = {"Vienas": "One", "Du": "Two", "Trys": "Three", "Keturi": "Four", "Penki": "Five",
           "Sesi": "Six", "Septyni": "Seven", "Astuoni": "Eight", "Devyni": "Nine"}
print("*"*40)
print(my_dict)

#Išrenkame žodyno indeksus
print("*"*40)
for item in my_dict:
    print(item)


#Išrenkame vertes pagal indeksus
print("*"*40)
for item in my_dict:
    print(my_dict[item])

#Išrenkame vertes
print("*"*40)
for item in my_dict.values():
for item in my_dict.keys():
    print(item)

#Išrenkamos indekso ir vertės poros
print("*"*40)
for item in my_dict.items():
    print(item)
for key, value in my_dict.items():
    print(key, value)



#Sukeičiame vertes ir indeksus vietomis
my_new_dict = {value: item for item, value in my_dict.items()}
my_new_dict = {value: key for key, value in my_dict.items()}
print("*"*40)
print()

print(my_dict)
print(my_new_dict)
