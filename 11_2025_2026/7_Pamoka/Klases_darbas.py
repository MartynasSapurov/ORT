#1 Užduotis
#Sukurkite tuščią sąrašą my_list
#Klaviatūra įveskite 10 vardų ne trumpesnių nei 5 simboliai atskirtų tarpais ir įrašykite į sąrašą pasitelkę split metodą
#Pasitelkę sąrašų generatorių sukurkite naują sąrašą my_new_list į kurį įtraukite visus įrašus iš my_list, bet tik simbolius nuo 3 iki paskutinio.
#Visui įrašai pateikiami didžiosiomis raidėmis
#Rezultatą atspausdinkite

#my_list = input("Įveskite vardus\n").split()
"""
my_list = "Kornėjus Daniel Augustas Maksim Natan Kajus Daniel Daniel Austėja Bernardas Emil".split()

my_new_list = [item[2:].upper() for item in my_list]

print(my_new_list)
"""

"""
#2 Užduotis
#Pasitelkę sąrašų generatorių sukurkite 20 atsitiktinių skaičių nuo 1 iki 9 sąrašąpavadinimu my_number_list
#Pasitelkę sąrašų generatorių atnaujinkite sąrašą pakeitę visus narius į jų kvadratą
import random

my_number_list = [random.randint(1, 9) for _ in range(20)]
print(my_number_list)
my_number_list = [item*item for item in my_number_list]
print(my_number_list)
"""
"""
#3 Užduotis
#Pasitelkę sąrašų generatorių sukurkite 10 narių žodyną kur indeskai būtų skaičiai nuo 0  iki 10, o vertės atsitiktiniai skaičiai tarp 1 ir 99
#Pasitelkę sąrašų generatorių tas žodyno vertes kurios mažesnės nei 20 padvigubinkite likusių nekeskite
import random

my_dict = {i: random.randint(1, 99) for i in range(10)}
print(my_dict)

my_dict = {key: value * 2 if value < 20 else value for key, value in my_dict.items()}
print(my_dict)
"""

#Savarankiška užduotis
#Įveskite 10 tarpu atskirtų verčių, skaičių ir raidžių ir įrašykite į sąrašą.
#Pasitelkę sąrašų generatorių patikrinkite ar elemntas skaičius, jei taip kobertuokite į int

txt = "50800"
x = txt.isdigit()
print(x)
