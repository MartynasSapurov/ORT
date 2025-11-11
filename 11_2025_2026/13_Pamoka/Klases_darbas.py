#Failą pavadinkite Darbas.py, atliktas užuotis užkomentuokite, pirmoje eilutėje nurodykite savo vardą
#
#
#1 Nuskaitykite duomeniš failo Animals.csv
#Jeigu gyvūnas yra tyras pakewiskite Amount į 17, jeigu ne 2
#Atsakymą įrašykite į failą Answer_1.csv

#2 Nuskaitykite duomeniš failų Safardi.txt ir Ashkenazi.txt iškoduokite simbolius ir
#abiejų sąrašų duomenis irašykite į failą Rabbi.txt

#3 Duotas Holokausto lietuvoje vietovardsąrašas
vietoves = [
    (b'Paneriai (Vilnius)', 70000, 0),
    (b'Kauno Devintas fortas', 50000, 0),
    (b'Kauno VII fortas', 3000, 0),
    (b'Kauno geto likvidavimas', 10000), 
    (b'\xc5\xa0iauli\xc5\xb3 geto likvidavimas', 8000, 1),
    (b'K\xc4\x97dainiai', 2000, 1),
    (b'Plung\xc4\x97', 1800, 1),
    (b'Tel\xc5\xa1iai / Raini\xc5\xb3 mi\xc5\xa1kas', 1500, 1),
    (b'Garg\xc5\xbedai', 200, 1),
    (b'Utena', 2000, 0),
    (b'Alytus', 1500, 0),
    (b'\xc5\xa0ven\xc4\x8dionys / \xc5\xa0ven\xc4\x8dion\xc4\x97liai', 3800, 1),
    (b'Panev\xc4\x97\xc5\xbeys', 8000, 1),
    (b'Marijampol\xc4\x97', 3800, 1), 
    (b'Jonava', 500, 0)
]
#sukurkite naują sąrašą į kurį įtraukti tik vietovardžiai su lietuviškais rašmenimis ir žuvusiųkų kiekis
liet_vietoves = []
#Įrašus sąraše atspausdinkite, kiekviena iš naujos eilutės
