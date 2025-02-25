def isvestis(sandauga):
    if sandauga > 100:
        print("Rezultatas per didelis")
    else:
        print(f"Sandauga: {sandauga}")

def daugyba(sk1, sk2):
    return sk1*sk2

def ivestis(pranesimas, bandymu_limitas=3, panaudotas_sk=None):
    for i in range(bandymu_limitas, 0, -1):
        sk=int(input(pranesimas))
        if sk%2 and sk>0:
            if sk!=panaudotas_sk:
                return sk
            else:
                print(f"Skaičius jau buvo įvestas! Bandymų liko: {i-1}")
        else:
            print(f"Klaida: Skaičius turi būti teigiamas ir nelyginis! Bandymų liko: {i-1}")
    print("Viršytas bandymų limitas! Programa baigiama")
    return None

sk1=ivestis("Įveskite pirmąjį nelyginį skaičių ")
if sk1 != None:
    sk2=ivestis("Įveskite antrąjį nelyginį skaičių ", panaudotas_sk=sk1)

if sk1 != None and sk2 != None:
    isvestis(daugyba(sk1, sk2))
