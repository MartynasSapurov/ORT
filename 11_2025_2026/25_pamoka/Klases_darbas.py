# Užduotis
# Sukurkurkite programą - žodyną, programa paprašytų klaviatūra įvesti kableliu atskirtą žodžių porą
# (tas pats žodis, tik skirtingomis kalbomis). Pirmasis žodis - žodyno indekssas, antrasis žodyno vertė.
# Po kiekvieno žodžio programa klaustų ar norite įvesti dar vieną žodžių porą, jei taip leistų įvesti dar vieną žodį
# ir pridėtų jį, prie jau anksčiau sukurto žodyno, jei ne įrašytų žodyną json formatu į failą

# Programą turi sudaryti bent šios funkcijos:
# 1. Sekos funkcija, kuri kartojasi tol, kol nepasirenkama, kad nenorite daugiau įvedinėti žodžių
# 2. Pirmosios funkcijos viduje lokali funkcija kuri atskiria kableliu atskirtus duomenis ir papilo žodyną
# Ši funkcija turi du argumentus, eilutę (string) kurią sudaro du atskirti kableliu žodžiai ir žodynas
# Funkcja paima praeitą žodyno versija į jį įterpią naujas vertes ir tuomet grąžina (naudokite lokalius kintamuosius)
# 3. Funkcija turi du argumentus: užpildytą žodyną ir failo pavadinimą.
# Ji įrašo žodyną į failą

# Sukurkite programą darbui su ankstesne programa sukurtu failu
# 4. Sukurkite programą kuri atsidarytų sukurtą json failą iš jo importuotų žodyną ir paklaustų vartotojo iš kurios kalbnos į kurią norėtų versti. 
# Jeigu pakeičiam kalba atskira funkcija kurios argumentas yra esamas žodynas pasitelkia sąrašų generatoriaus konstrukciją ir grąžina žodyną sukeisdama indeksus su vertėmis.


# Create a dictionary
my_dict = {'One': 'Vienas', 'Two': "Du"}

# Add a new member
my_dict["Three"] = "Trys"

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

a = int(input())

def mano_funkcija(b):
    result = b*b
    return result

print(mano_funkcija(a))

my_dict = {"Lion":"אַרְיֵה", "Lamb": "כֶּבֶשׂ", "Dove":"יוֹנָה"}
my_dict = {value: key for key, value in my_dict.items()}
print(my_dict)
