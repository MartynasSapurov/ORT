#Darbas su sąrašais (kortežais) ir for ciklas, range() funkcijos taikymas

my_tuple = ("One", "Two", "Three", "Four", "Five")

#Duomenų išvedimas for ciklu netaikant range()
print("*"*40)

for item in(my_tuple):
    print(item)

#Duomenų išvedimas taikant režius [::]
#Išvedame narius nuo antrojo iki prieš paskutinio ("Three", "Four")
print("*"*40)
for item in my_tuple[2:-1]:
    print(item)

#arba
print("*"*40)
for item in my_tuple[2: len(my_tuple) - 1]:
    print(item)

#Išvedame narius nuo antrojo iki prieš paskutinio ("Three", "Four") taikant range funkciją
print("*"*40)
for i in range(2, len(my_tuple) - 1):
    print(my_tuple[i])

#Išvedame kas antrą narį atbuline tvarka ("Five", "Three", "One")
print("*"*40)
for item in my_tuple[-1::-2]:
    print(item)

#arba
print("*"*40)
for item in my_tuple[len(my_tuple) - 1::-2]:
    print(item)

#Išvedame kas antrą narį atbuline tvarka ("Five", "Three", "One") taikant range funkciją
print("*"*40)
for i in range(len(my_tuple) - 1, -1, -2):
    print(my_tuple[i])
