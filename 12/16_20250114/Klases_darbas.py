class gimtadienis(object):
    def __init__(self, pavadinimas, ingridientai):
        self.pavadinimas = pavadinimas
        self.ingridientai = ingridientai

    def kaina(self, produktu_kainos, ingridientu_kiekis):
        kaina = 0
        for i in range(ingridientu_kiekis):
            kaina += produktu_kainos[i] * self.ingridientai[i]
        return kaina

def bendra_kaina(patiekalo_kaina, ):
    kaina

with open("U2.txt", 'rt') as duomenys:
    ingridientu_kiekis, patiekalu_kiekis = [int(item) for item in duomenys.readline().split()]
    produktu_kainos = [int(item) for item in duomenys.readline().split()]
    menu = []
    for i in range(patiekalu_kiekis):
        duomeys_is_failo = duomenys.readline()
        patiekalo_pavadinimas = duomeys_is_failo[:15]
        patiekalo_ingridientai = [int(item) for item in duomeys_is_failo[15:].split()]
        menu.append(gimtadienis(patiekalo_pavadinimas, patiekalo_ingridientai))

#for item in menu:
#    print(item.pavadinimas)

with open("result.txt", "wt") as result:
    bendra_kaina = 0
    for item in menu:
        result.write(f"{item.pavadinimas}{item.kaina(produktu_kainos, ingridientu_kiekis)}\n")
        bendra_kaina += item.kaina(produktu_kainos, ingridientu_kiekis)
    result.write(f"{int(bendra_kaina/100)} {bendra_kaina%100}")
