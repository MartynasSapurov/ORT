from random import randint as random
#Pasitelkę sąrašų generatorių sukurkite 1000 atsitikrinių skaičių nuo 0 iki 99 sąrašą
my_number_list = [random(0, 99) for i in range(1000)]
#Sąrašą surušiuokite ir pasitelkę time biblioteką išmatuokite kiek trunka sąrašo surūšiavimas
