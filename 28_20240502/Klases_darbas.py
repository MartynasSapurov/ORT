#1
#list generator
my_list = [1, 2, 3, 4, 5]

my_new_list = [item for item in my_list]
print(my_new_list)

Parašykite lambda funkcija kuri nuskaitytų duotą sąrašą ir jei pirmoji žodžio sąraše raide = 'a' arba 'A' grąžintų
pasutinius tris simbolius didžiosiomis raidėmis, jei pirmoji radė nelygi 'a' arba 'A' grąžintų pirus tris simbolius mažosiomis raidėmis.

['Albert', 'bob', 'Robert', 'aliona', 'Algirdas', 'alicija', 'UZDUOTIS', 'pirmSiS']

#3
Duotas s1rašas sudarytas iš skirtingų tipų duomenų.
Taikydami map() funkciją parašykite programą kuri grąžintų sąrašą kuriame kiekvienas int tipo kintamasis būtų pakeistas į str tipą,
visus kitų tipų elemntūs įkelkite į sąrašą nekeisdami. Duomenų pakeitimui map funkcijos visuje panaudokite lambda funkciją.

values = [1, 2, '3', 'forth', 'end', 99, True, None]

#3
Taikydami filter() funkciją iš ždžių sąrašo išrinkite tikt tuos, kurie yra polindromai (skaitomi vienodai iš abiejų pusių),
programa turi nekreipti dėmesio į tai raidės didžiosios ar mažosios. Duomenims atrinkti taikykite lambda funkcijas.


inputdata = ['alus', 'eme', 'sava', 'valstybe', 'palapine', 'kroliai', 'sula', 'namai', 'kalba']
