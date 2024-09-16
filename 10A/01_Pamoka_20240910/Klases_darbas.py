print("Hello world")
print("*"*80)

#Kelių teksto atkarpų spausdinimas nurodomas print funkcijoje atskiriant šias atkarpas kableliais
print("Laba diena, mano vardas", "Martynas")
print("*"*80)

#Atkiriant teksto atkarpas kableliu automatškai įterpiamas vieno tarpelio skirtukas, jį galima pakeisti
#bet kurio simboliu, pavyzdžiui "$"
print("Laba diena, mano vardas", "Martynas", sep="$")
print("*"*80)

#arba naujois eilut4s skirtuku "\n"
print("Laba diena, mano vardas", "Martynas", sep="\n")
print("*"*80)

#Kelias teksto atkarpas galima spausdinti ir atskiromis print komandomis, kiekviena jų teksto pabaigoje įterpia
#naujos eilutės simbolį
print("Laba diena, mano vardas")
print("Martynas")
print("*"*80)

#Pabaigos sibolį taip pat galime keisti savo nuožiūra, pavyzdžiui į "$"
print("Laba diena, mano vardas", end="$")
print("Martynas")
print("*"*80)

#Naujos eilutės ir kitus specialius simbolius galima įterpti ir tiesiai į tekstą
print("Mūsų mokykla\n yra pati\n  geriausia")
print("*"*80)

#Kintamasis yra atminties ląstelė skirta saugoti tam tikrai informacijai,
#pradžiai susipažnsime su 3 pagrindiniais jų tipais:
#integer(int) - sveikasis skaičius
#float - trupmeninis kaičius
#string(str) - simbolių eilutė, tekstas
#kintamojo tipą grąžina dunkcija type(), o adresą atmintyje funkcija id()

skaicius = 5
trupmeninis_skaicius = 5.8
tekstas = "Labas rytas"

print(skaicius, type(skaicius), id(skaicius))
print("*"*80)
print(trupmeninis_skaicius, type(trupmeninis_skaicius), id(trupmeninis_skaicius))
print("*"*80)
print(tekstas, type(tekstas), id(tekstas))
print("*"*80)
