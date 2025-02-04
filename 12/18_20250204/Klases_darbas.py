#Duotas failas U1.txt, jame pateikta informacija apie krepšininkus, pirmoje eilutėje nurodoma, kiek yra įrašų, visose
#kitose pirmas skaičius žaidėjoi numeris, antras skaičius nurodod kiek eilutėje įrašų apie žaidėją, vėliau seka
#žaistas laikas (teigiami skaičiai), praleistas laikas neigiamis kaičiai
#1. Perskaitykite iš failo pirmąjį įrašą ir atspausdinkiyte ekrane įrašų skaičių

#2.Nuskaitykite tik zaideju numerius į sąrašą zaidejai ir jį surūšiuokite

#3.Pridėkite papildomus narius (visą eilutę duomenų į sūrūšiuotą sąrašą, tai kad prie žaidėjo numerio atsirastų
#informaciją apie žaistas minutes

#4.patikrinkite visų žaidėjų visus laikus (tik tiek laikų kiek nurodyta antruoju skaičiumi) ir pridėkite prie saraso
#papildomus du skaicius (žasita ir praleista minučių)

#5. Atspausdinkite, tik žaidėjo numerį viso žaista ir viso praleistą iš sukurto sątašo į failą rez1.txt

with open("U1.txt", 'rt') as duomenys:
    irasau_skaicius = int(duomenys.readline())
    print(irasau_skaicius)
    zaidejai=[]
    zaidejai_nerusiuoti = []
    zaidejai_full = []
    for _ in range(irasau_skaicius):
        nerusiuoti_duomenys =  list(map(int, duomenys.readline().split()))
        zaidejai_nerusiuoti.append(nerusiuoti_duomenys)
        zaidejai.append(nerusiuoti_duomenys[0])
    zaidejai = sorted(zaidejai)

for item in zaidejai:
    print(item)
    for item2 in zaidejai_nerusiuoti:
        if item == item2[0]:
            zaidejai_full.append(item2)


for item in zaidejai_full:
    zaista = 0
    praleista = 0
    for _ in range(2, item[1]+2):
        if item[_] > 0:
            zaista += item[_]
        else:
            praleista += abs(item[_])
    item.append(zaista)
    item.append(praleista)

with open("result.txt", "wt") as result:
    bendra_kaina = 0
    for item in zaidejai_full:
        result.write(f"{item[0]}{item[item[1]+2], item[item[1]+3]}\n")
