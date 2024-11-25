#Pasitelkę sąrašų generatorių sukurkite 100000 atsitikrinių skaičių nuo 0 iki 99 sąrašą
my_unsorted_list = [random(0, 99) for i in range(100000)]

my_list_for_sorting = my_unsorted_list
#Sąrašą surušiuokite ir pasitelkę time biblioteką išmatuokite kiek trunka sąrašo surūšiavimas
start_time = time()
my_list_for_sorting.sort()
time_delta=time() - start_time
print(time_delta)

#Sukurkit klasę kurioje bus vienas atributas ir vienas metodas, atributas yra tuščias sąrašas į kurį
#objekto kūrimo metu įrašomas nerūšiuotas sąrašas, o metodas surūšiuoja sąrašą burbulo rušiavimo algoritmu
