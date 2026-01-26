"""
#1 Duotas sąrašas
my_list = [2, 11, 25, 13, 55, 17, 45, 85, 45, 128, 85, 48]
#Taikydami filter ir lambda funkcijas sukurkite naują sąrašą į kurį patektų tik lyginiai skaičiai

my_list = list(filter(lambda x: x % 2 == 0, my_list))

print(my_list)
"""
"""
#2 Duotas sąrašas
my_list = [2, 11, 25, 13, 55, 17, 45, 85, 45, 128, 85]
#Taikydami map ir lambda funkcijas sukurkite naują sąrašą kurį sudarytų duotų skaičių vertės padauginos iš 6

my_list = list(map(lambda x: x*6, my_list))

print(my_list)
"""
"""
#3 Duoti du sąrašai
my_data_1 = [8, 4 , 11, 15, 52, 45, 12]

my_data_2 = [1, 17, 25, 45, 11, 12, 13]
#Taikydami map funkciją sukurkite naują sąrašą, kurį sudarytų šių sąrašų elementų skirtumai
my_list = list(map(lambda x, y: x-y, my_data_1, my_data_2))
print(my_list)
"""

#4 Nuskaitykite teksto ilutę, pavyzdžiui
"""
11A ir 11B klasėse mokosi patys geriaus Šolomo Aleichemo ORT gimnazijos programuotojai!
"""
#Padalinkite šią eilutę į atskirus 15 simbolių segmentus, paskutiniame segmente turi likti likutis <= 15.
#Segmentų skaičius turi priklausyti nuo eilutės ilgio
#Rezultat1 5ra6ykite į fsailą Result_3.txt, kiekvienas segmentas spausdinamas iš naujos eilutės
#Rezultato failo pavyzdys

my_line = input()
my_list = [item for item in my_line]
for i in range(len(my_list)):
    print(f"{i} {my_list[i]}")


"""
11A ir 11B klas
ėse mokosi paty
s geriaus Šolom
o Aleichemo ORT
gimnazijos prog
ramuotojai!
"""
