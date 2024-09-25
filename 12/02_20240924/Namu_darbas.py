"""
with open('U1.txt', 'rt') as file:
    my_list = [[int(item) for item in items.split()] for items in file.readlines()[1:]]
    print(my_list)
    #my_list = file.readline().split()
    #my_list = [int(item) for item in my_list]
    #print(my_list)
"""
"""
line = []
with open('U1.txt', 'rt') as file:
    n=int(file.readline())
    print(n)
    for i in range(n):
        line.append([int(item) for item in file.readline().split()])
    print(line)
"""
#PPateikti du duomenų išrinkimo iš failo algoritmai, pasirinkite bet kurį. Pasinaudoję gautu dvimačiu masyvu (dviejų lygmenų sąrašu) sukurkite
#naują sąrašą arba žodyną kuriame būtų pateikiama suminė statistika (duomenų apie varžybas suma, pvz.: kiek pataikytų tritaškių per visas sužaistas varžybas)
#apie kiekvieną žadėją: žaidėjo numeris(kartojasi tik vieną kartą ir suminiai duomenys apie
#visas rungtynes, taip pat pridėkite papildomą laukelį kuriame nurodomas sužaistų rungtynių skaičius (kiek rungtini sužaidė konkretus žaidėjas).

Duomenų išaiškinimas
23 3 3 3 5 0 0
23 - Žaidėjo nr
3 - pataikytų baudinių sk
3 - mestų baudinių sk
3 - pataikytų dvitaškių sk
5 - mestų dvitaškių sk
0 - pataikytų tritaškių sk
0 - mestų tritaškių sk
