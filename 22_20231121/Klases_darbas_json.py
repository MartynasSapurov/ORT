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

