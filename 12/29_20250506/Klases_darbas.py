def dienos_numeris(menuo, diena):
    if menuo==6:
        return diena
    elif menuo==7:
        return diena+30
    elif menuo==8:
        return diena+61
    else:
        return 0

vasaros_dienos = 92

with open("U1.txt", 'rt') as duomenys:
    geliu_kiekis = int(duomenys.readline())

    geles = []
    for _ in range(geliu_kiekis):
        nuskaityti_duomenys=list(map(int, duomenys.readline().split()))
        geles.append([nuskaityti_duomenys[0], dienos_numeris(nuskaityti_duomenys[1], nuskaityti_duomenys[2]),
                      dienos_numeris(nuskaityti_duomenys[3], nuskaityti_duomenys[4])])
    print(geles)

geliu_zydejimas = {item: 0 for item in range(1, vasaros_dienos+1)}

print(geliu_zydejimas)


for i in range(1, vasaros_dienos+1):
    for item in geles:
        if i >= item[1] and i <= item[2]:
            geliu_zydejimas[i]+=1



print(geliu_zydejimas)
(max(geliu_zydejimas.values()))
max_zydejimas = {item[0]: item[1] for item in geliu_zydejimas.items() if item[1]== max(geliu_zydejimas.values())}
print(max_zydejimas)
