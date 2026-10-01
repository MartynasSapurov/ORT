#Pasitelkę sąrašų generatorių sukurkite 10000 atsitikrinių skaičių nuo 0 iki 99 sąrašą
my_unsorted_list = [random(0, 99) for i in range(10000)]

my_list_for_sorting = my_unsorted_list
#Sąrašą surušiuokite ir pasitelkę time biblioteką išmatuokite kiek trunka sąrašo surūšiavimas
start_time = time()
my_list_for_sorting.sort()
time_delta=time() - start_time
print(time_delta)

#Sukurkit klasę kurioje bus vienas atributas ir vienas metodas, atributas yra tuščias sąrašas į kurį
#objekto kūrimo metu įrašomas nerūšiuotas sąrašas, o metodas surūšiuoja sąrašą burbulo rušiavimo algoritmu
#palyginkite algotitmų veikimo trukmę

my_list=[1, 18, 7 ,48, 10, 14, 15]

for i in range(n):
    didesnis=False
    print(my_list)
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] =  my_list[j+1], my_list[j]
            didesnis=True
    if (didesnis==False):
        break
