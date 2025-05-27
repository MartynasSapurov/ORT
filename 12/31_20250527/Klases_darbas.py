with open("U2.txt", 'rt') as duomenys:
    dienu_kiekis = int(duomenys.readline())
    pratimai = []
    for i in range(dienu_kiekis):
        nuskaityt_duomenys = duomenys.readline().split()
        atlikta_pratimu = int(nuskaityt_duomenys[0])
        offset = 0
        for j in range(atlikta_pratimu):
            pratimai.append([nuskaityt_duomenys[1+offset].ljust(14),
                             nuskaityt_duomenys[2+offset].ljust(7),
                             int(nuskaityt_duomenys[3+offset])])
            offset+=3
print(pratimai)

pratimu_zodynas = {item[0]:[0, 0, 0, 0, 0] for item in pratimai}

for item in pratimu_zodynas.keys():
    for pratimas in pratimai:
        if item == pratimas[0]:
            pratimu_zodynas[item][0]+=1
            pratimu_zodynas[item][1]+=pratimas[2]
            

print(pratimu_zodynas)
