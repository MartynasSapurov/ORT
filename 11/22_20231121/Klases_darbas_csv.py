#Darbas su scv (comma-separated values) failais

import csv #Importuojame csv biblioteką

name_of_fields = ["Name", "Grade", "Age"] #Sukuriame duomenų antraštes
field_01 = ["Peter", "3", "10"] #Pirmoji duomenų eilutė
field_02 = ["John, Michael", "", "12"] #Antroji duomenų eilutė
field_03 = ["George", "11", "18"] #trečioji duomenų eilutė

#Duomenų įrašymas CSV formatu
with open("data.csv", mode='w', encoding='utf8', newline='') as file: #Atsidarome failą rašymui, pakeičiame nustatymus,
# kad nebūtų perkialiama nauja eilutė newline=''
    file_writer = csv.writer(file) #Susikuriame csv failo rašymo konstruktorių
    file_writer.writerow(name_of_fields) #Įrašome antraštinę eilutę
    file_writer.writerow(field_01) #Įrašome pirmają duomenų eilutę
    file_writer.writerow(field_02) #Įrašome antrąją duomenų eilutę
    file_writer.writerow(field_03) #Įrašome trečiąją duomenų eilutę

#CSV duomenų nuskaitymas
with open("data.csv", encoding='utf8') as file: #Atsidarome failą skaitymui
    file_reader = csv.reader(file) #Susikuriame csv failo skaitymo konstruktorių
    for item in file_reader: #Atspausdiname visus nuskaitytus duomenis
        print(item) #Atkreipkite dėmesį, kad kiekviena duomenų eilutė nuskaitoma, kaip sąrašas (list)
        #jeigu norėtume atspausdinti George amžių tūrėtume parašyti print(list(file_reader)[3][1])
        #Visų pirma pasikonvertuojame objektą csv.reader į sąrašą, o tada norodome mus dominančius duomenis
