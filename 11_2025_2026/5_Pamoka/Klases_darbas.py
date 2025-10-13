import random

my_number_list = []

for _ in range(20):
    my_number_list.append(random.randint(1, 99))

print(my_number_list)

for i in range(len(my_number_list)):
    my_number_list[i] += 5

print(my_number_list)

my_string_list = []
for _ in range(20):
    my_string_list.append(str(random.randint(1, 99)))

print(my_string_list)
"""
for i in range(len(my_string_list)):
    my_string_list[i] = int(my_string_list[i])

print(my_string_list)
"""
"""Sąrašu generatoriai"""

#my_generated_list  = [random.randint(1, 99) for i in range(20)]
my_generated_list  = [item for item in my_string_list[::-1]]
print(my_generated_list)
print(40*"*")
print(my_string_list)
print(my_generated_list)

n = int(input())

"""
if n % 2 == 0:
    print("Lyginis")
else:
    print("Nelyginis")
"""
print("Lyginis") if n % 2 == 0 else print("Nelyginis")

#Savaranki6ka užduotis
#Sukurkite 30 atsitiktinių skaičių, tarp 1 ir 150, sąrašą, pasitelkę.
#asirelkę sąrašų generatorių perkelkite į naują sąčrašą tik skaičius didesnius nei 80

