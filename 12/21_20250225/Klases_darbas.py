with open("U1.txt", 'r') as duomenys:
    imoniu_skaicius, kilometru_limitas = map(int, duomenys.readline().split())
    imones = {}
    for _ in range(imoniu_skaicius):
        nuskaityta_eilute = duomenys.readline()
        imone = nuskaityta_eilute[:10]
        koordinates = [abs(int(item)) for item in nuskaityta_eilute[10:].split()]
        imones[imone] = koordinates

nuvaziuotas_atstumas = 0
aplankytu_imoniu_kiekis = 0

for item in imones.keys():
    if  nuvaziuotas_atstumas+2*(imones[item][0]+imones[item][1]) <= kilometru_limitas:
        nuvaziuotas_atstumas+=2*(imones[item][0]+imones[item][1])
        aplankytu_imoniu_kiekis+=1
        item_old=item
    else:
        break

with open("U1_Rez.txt", 'w') as rezultatai:
    rezultatai.write(f"{aplankytu_imoniu_kiekis} {nuvaziuotas_atstumas} {item_old}")
