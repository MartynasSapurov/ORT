#Duotas duomenų kortežas
my_tuple = ("Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n", "Line 6\n", "Line 7\n", "Line 8\n")
#1. Užduotis
#Taikydami for ciklą sukurkite failą my_file.txt kuriame kiekvienas kortežo narys rašomas iš naujos eilutės

#2. Užduotis
#Papildomai į failą my_file.txt įrašykite naują eilutę su tekstu "Line 9"

#3. Užduotis
#Taikydami metoda .read() atspausdinkite 2-6 antrosios eilutės simbolius

#4. Užduotis
#Taikydami metoda .readline() atspausdinkite 2, 5 eilutes ir paskutinius 2 aštuntos eilutės simbolius

#5. Užduotis
#Taikydami for ciklą ir metoda .readlines() atspausdinkite 2, 5 eilutes ir paskutinius 2 aštuntos
#eilutės simbolius

#Atlikdami užduotis privalote panaudoti visas tris darbo su failas konstrukcijas
#(kiekvienai užduočiai atlikti taikykite skirtingas konstrukcijas)

#Papildoma neprivaloma užduotis: 4 ir 5 u-duotyse pakeskite print funkciją taip, kad nebūtų spausdinamos tuščios eilutės

#Darbo su failais konstrukcijos
"""
file = open('file.txt', 'r')
file.close()

with open('file.txt', 'r') as file:

try:
    file = open('file.txt')
finally:
    file.close()
"""