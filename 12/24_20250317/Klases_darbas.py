def pasiektas_tikslas(pradzios_koordinates, tikslo_koordinates, komandu_seka):
    keliones_eiga = [0, 0]
    keliones_eiga[0], keliones_eiga[1] = pradzios_koordinates[0], pradzios_koordinates[1]
    for i in range(1, komandu_seka[0]+1):
        if komandu_seka[i]==1:
            keliones_eiga[1]+=1
        elif komandu_seka[i]==2:
            keliones_eiga[0] += 1
        elif komandu_seka[i] == 3:
            keliones_eiga[1] -= 1
        elif komandu_seka[i] == 4:
            keliones_eiga[0] -= 1
        if keliones_eiga == tikslo_koordinates:
            return ["Pasiektas tikslas", i]
    return ["Sekos pabaiga", i]

with open("U2.txt", 'rt') as duomenys:
    pradzios_koordinates = [int(item) for item in duomenys.readline().split()]
    tikslo_koordinates = list(map(int, duomenys.readline().split()))
    komandu_seku_skaicius = int(duomenys.readline())
    komandu_sekos = []
    for _ in range(komandu_seku_skaicius):
        nuskaityt_duomenys = list(map(int, duomenys.readline().split()))
        komandu_sekos.append(nuskaityt_duomenys[0:nuskaityt_duomenys[0]+1])

with open("U2rez.txt", 'wt') as result:
    for i in range(komandu_seku_skaicius):
        rezultatai = pasiektas_tikslas(pradzios_koordinates, tikslo_koordinates, komandu_sekos[i])
        komandu_sekos_str = list(map(str, komandu_sekos[i][1:rezultatai[1]+1]))
        komandu_sekos_str = " ".join(komandu_sekos_str)
        result.write(f"{rezultatai[0]} {komandu_sekos_str} {rezultatai[1]}\n")
