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
