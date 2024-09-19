"""#Namų darbas
#Duoti trys kintamieji
skaicius = 5
trupmeninis_skaicius = 5.8
tekstas = "Labas rytas"

#Taikant type() ir id() funkcijas galima atspausdinti šių kintamųjų vertes, tipus ir adresus atmintyje
print("Kintamojo \"skaičius\" vertė = \"", skaicius, "\", tipas = \"", type(skaicius), "\", o adresas = \"",
      id(skaicius), "\"",  sep="")
print("*"*80)
#print(trupmeninis_skaicius, type(trupmeninis_skaicius), id(trupmeninis_skaicius))
print("Kintamojo \"trupmeninis_skaicius\" vertė = \""+str(trupmeninis_skaicius)+", tipas = "+str(type(trupmeninis_skaicius))
      +", o adresas = "+str(id(trupmeninis_skaicius)))
print("*"*80)
#print(tekstas, type(tekstas), id(tekstas))
print("Kintamojo \"tekstas\" vertė = \"%s\", tipas = \"%s\", o adresas = \"%d\""
      %(tekstas, type(tekstas), id(tekstas)))
print("*"*80)

print(f"Kintamojo \"skaičius\" vertė = \"{skaicius}\", tipas = \"{type(skaicius)}"
      f"\", o adresas = \"{id(type(skaicius))}\"")

#Patobulinkite pateiktą kodo atkarpą taip, kad šie duomnys būtų spausdinami pateikiant aiškų ir rišlų tekstą
#(atkreipkite dėmesį, kad norint atspausdint sibolį ", jis nurodomas su pasvyruoju brūkšneliu \")
#rezultatas tururėtų atrodyti taip:"
"""
"""
Kintamojo "skaičius" vertė = "5", tipas = "<class 'int'>", o adresas = "140722714909240"
********************************************************************************
Kintamojo "trupmeninis_skaicius" vertė = "5.8", tipas = "<class 'float'>", o adresas = "2458351086704"
********************************************************************************
Kintamojo "tekstas" vertė = "Labas rytas", tipas = "<class 'str'>", o adresas = "2458355027056"
********************************************************************************
"""

    sk_1 = int(input("Įveskite pirmąjį skaičių: "))

sk_2 = int(input("Įveskite antrąjį skaičių: "))
print(f"Jūsų įvestų skaičių suma: {sk_1}+{sk_2}={sk_1+sk_2}")
"""
1.Sraigė per valandą nušliaužia z žiogo šuolių. Žiogas vienu šuoliu nušoka c centimetrų. Kiek centimetrų
sraigė nušliauš per v valandų? Parašykite programą šiam uždaviniui spręsti.
Pasitikrinkite. Kai z = 2, c = 2, v = 8, tai turi būti spausdinama 32.
2. Laivynas iš k laivų, kurių kiekvienas plukdė po n maišų prieskonių, pakliuvo į audrą, kurioje m laivų
nuskendo, o kiti sėkmingai pasiekė kelionės tikslą. Kiek maišų prieskonių pavyko parvežti?
Pasitikrinkite. Kai k = 15, n = 8000 , m = 3, tai pavyko parvežti 96000 maišų prieskonių.
3. Per kiek laiko tamsiame urve paklydęs turistas vieną po kito sudegins n degtukų, jei kiekvienas iš jų dega m
minučių? Atsakymą išreikškite valandomis ir minutėmis.
Pasitikrinkite. Kai n = 75, m = 2 , tai degtukai sudegs per 2 val. ir 30 min.
4. Laikrodis rodo x valandų ir y minučių. Parašykite programą, kuri apskaičiuotų, kiek minučių minut ir
kiek sekundžių sec prabėgo nuo vidurnakčio.
Pasitikrinkite. Įvedę x = 3 ir y = 5, turėtumėte gauti: minut = 185, sec = 11100.
"""
