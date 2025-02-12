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
                print(f"Skaičius jau buvo įvestas! Bandymų liko: {bandymu_limitas-1}")
        else:
            print(f"Klaida: Skaičius turi būti teigiamas ir nelyginis! Bandymų liko: {bandymu_limitas-1}")
    print("Viršytas bandymų limitas! Programa baigiama")
    return None

sk1 = ivestis("Įveskite pirmą teigiamą skaičių: ")
if sk1 != None:
    sk2 = ivestis("Įveskite antrą teigiamą skaičių: ", panaudotas_sk=sk1)
    isvestis(daugyba(sk1, sk2))
