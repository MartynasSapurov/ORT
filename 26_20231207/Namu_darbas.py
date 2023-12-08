# Darbas su funkcijomis ir jų matymo srytimi.
# Funkcijos, kaip ir kintamieji gali būti teik lokalūs, tiek globalūs, pavyzdžiui
def my_global_function_1():
    print("Hi I am global function 1")
    return 0


def my_global_function_2():
    print("Hi I am global function 2")
    return 0
# Abi parodytos funkcijos yra globalios ir gali būti vykdomos tiek pagrindinėje programoje tiek funkcijos viduje:


my_global_function_1() # Funkcijos vykdomos pagrindinėje prograoje
my_global_function_2() # Funkcijos vykdomos pagrindinėje prograoje


def my_global_function_3(): # Tai yra globali funkcija kuri vykdo savo viduje kita globalias funkcijas
    print("I am local function 3 and I can execute other global functions")
    my_global_function_1() # Globalios funkcijos vykdomos kitoje funkcijoje
    my_global_function_2() # Globalios funkcijos vykdomos kitoje funkcijoje
    return 0


my_global_function_3() # Globalios funkcijos vykdomos kitoje funkcijoje

# Taip pat funkcija gali būti aprašoma kitoje funkcijoje, tokiu atveju ji yra lokali
# ir gali būti vykdoma tik tos funkcijos, kurioje ji yra sukurta, viduje


def my_global_function_4():
    def my_local_function_1(): # Lokali unkcija, kitos funkcijos viduje
        print("Hi I am local function 1 I am inside global function 4")
    print("Hi I am global function 4")
    my_local_function_1() # Lokalios funkcijos vykdymas
    return 0


my_global_function_4() # Globalios funkcijos vykdomos kitoje funkcijoje

#Jeigu pabandytume 5vykdyti žemiau pateiktą interpretatorius sugeneruotų klaidą,
# nes bandome įvykdyti lpkalia funkciją globalioje srityje

# my_local_function_1() # Lokalios funkcijos vykdymas

# Namų darbo užduotys:
# 1. Užduotis
# Sukurkurkite programą - žodyną, programa paprašytų klaviatūra įvesti kableliu atskirtą žodžių porą
# (tas pats žodis, tik skirtingomis kalbomis). Pirmasis žodis - žodyno indekssas, antrasis žodyno vertė.
# Po kiekvieno žodžio programa klaustų ar norite įvesti dar vieną žodžių porą, jei taip leistų įvesti dar vieną žodį
# ir pridėtų jį, prie jau anksčiau sukurto žodyno, jei ne įrašytų žodyną json formatu į failą

# Programą turi sudaryti nbent šios funkcijos:
# 1. Sekos funkcija, kuri kartojasi tol, kol nepasirenkama, kad nenorite daugiau įvedinėti žodžių
# 2. Pirmosios funkcijos viduje lokali funkcija kuri atskiria kableliu atskirtus duomenis ir papilo žodyną
# Ši funkcija turi du argumentus, eilutę (string) kurią sudaro du atskirti kableliu žodžiai ir žodynas
# Funkcja paima praeitą žodyno versija į jį įterpią naujas vertes ir tuomet grąžina (naudokite lokalius kintamuosius)
# 3. Funkcija turi du argumentus: užpildytą žodyną ir failo pavadinimą.
# Ji įrašo žodyną į failą

# Svarbu, kad dirbtum4te su lokaliais kintamaisiais ir funkcijomis, kad suprastūmėte, kaip veikia retun funkcija
