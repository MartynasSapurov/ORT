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
# 5. Parašykite atskirą funkcija kuri paprašytų įvesti žodį ir grąžintų reikšmę, taip pat pritaikykite konstrukcija try, except, kad tokiu atveju, kai žodis nerastas parašytų "Nėra tokio žodži

# Create a dictionary
my_dict = {'name': 'Alice', 'age': 25}

# Add a new member
my_dict['city'] = 'Vilnius'
