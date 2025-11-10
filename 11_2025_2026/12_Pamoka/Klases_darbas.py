import csv #Importuojame csv biblioteką

name_of_fields = ["Vardas", "Pavardė", "Gimimo data"]
duomenys  = [["Kajus",  "Kilšauskas", "2007-10-23"], ["Daniel", "Gustaitis", "2008-05-20"], ["Emil", "Čeliadin", "2008-04-16"],
             ["Maksim", "Rudek", "2008-03-26"], ["Kornėjus", "Pozdniakovas", "2008-04-05"]]

for item in duomenys:
    print(item)

#Duomenų įrašymas CSV formatu
with open("data.csv", mode='w', encoding='utf8', newline='') as file: #Atsidarome failą rašymui, pakeičiame nustatymus,
# kad nebūtų perkialiama nauja eilutė newline=''
    file_writer = csv.writer(file) #Susikuriame csv failo rašymo konstruktorių
    file_writer.writerow(name_of_fields) #Įrašome antraštinę eilutę
    for item in duomenys:
        file_writer.writerow(item) #Įrašome pirmają duomenų eilutę

#CSV duomenų nuskaitymas
with open("data.csv", encoding='utf8') as file: #Atsidarome failą skaitymui
    data = csv.reader(file) #Susikuriame csv failo skaitymo konstruktorių
    print(40*"*")
    csv_data = [item for item in list(data)[1::]] 

print(csv_data)
"""
Tik duomenis iš csv failo be antraštės įkelkite į sąrašą pavadinimu csv_data ir jį atspausdinkite
"""

