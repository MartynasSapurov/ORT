#Darbas su csv (comma-separated value)
"""
import csv

name_of_fields = ["Eil, nr", "Vardas", "Batų dydis", "Amžius", "Pištų kiekis"]
line_1 = [1, "Kajus", 43, 18, 20]
line_2 = [2, "Austėja", 40, 17, 20]
line_3 = [3, "Budnikas", 44, 17, 19.5]
line_4 = [4, "Golod", 42, 18, 19.99]

#Duomenų įrašymas
with open("11AB.csv", mode="w", encoding="utf8", newline="") as AB11_csvfile:
    file_writer = csv.writer(AB11_csvfile)
    file_writer.writerow(name_of_fields)
    file_writer.writerow(line_1)
    file_writer.writerow(line_2)
    file_writer.writerow(line_3)
    file_writer.writerow(line_4)

#Duomenų nuskaitymas
with open("11AB.csv", mode="r", encoding="utf8", newline="") as AB11_csvfile:
    file_reader = csv.reader(AB11_csvfile)
    for item in file_reader:
        print(item)
"""
#Darbas su json (JavaScript Object Notation) failais
import json #Importuojame json biblioteką

input_data = ("Alef", "Beit", "Gimel", "Dalet", "He")
#Duotas užpildytas kortežas

with open('data.json', 'w') as file: #Atsidarome failą rašymui
  json.dump(input_data, file) #Įrašome mūsų kortežą į failą

with open('data.json') as file: #Atsidarome failą rašymui
  output_data = json.load(file) #Nuskaitome duomenis iš failo

print(output_data) #Atspausdiname nuskaitytus duomenis
print(type(output_data)) #Atspausdiname nuskaitytų duomenų tipą
#Atkreipkite dėmesį, kad nuskaityto duomenys yra nebekortežas o sąrašas, nes json automatiškai konvertuoja į sąrašus,
#todėl, kad neturi tokio duomkenų tipo

#Taip pat galima taikyti json.dumps() konstrukciją, kai duomenys paverčiami eilute (string)
string_data = json.dumps(input_data)
print(string_data) #Atspausdiname konvertuotus duomenis
print(type(string_data)) #Atspausdiname kobvertuotų duomenų tipą
