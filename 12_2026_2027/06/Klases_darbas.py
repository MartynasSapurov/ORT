class dievai(object):
    def __init__(self, vardas, metimu_sk, metimai, eil_nr):
        self.vardas=vardas
        self.metimu_sk=metimu_sk
        self.metimai=metimai.copy()
        self.eil_nr=eil_nr
        self.taskai=0
        self.lyginiai=0

    def print_data(self):
        print(f"Eil. nr.: {self.eil_nr} vardas: {self.vardas}, {self.metimu_sk} metimai: {self.metimai}, {self.taskai} taskai, {self.lyginiai} lyginiai")

    def skaiciavimas(self):
        for i in range(self.metimu_sk):
            if  not(self.metimai[i] % 2):
                self.taskai += self.metimai[i]
                self.lyginiai+=1
            else:
                self.taskai -= self.metimai[i]

with open("U2.txt") as file:
    dievu_sk, metimu_sk = map(int, file.readline().split())
    olimpo_dievai=[]
    for i in range(dievu_sk):
        line = file.readline()
        vardas = line[:10]
        metimai = list(map(int, line[11:].split()))
        olimpo_dievai.append(dievai(vardas, metimu_sk, metimai, i))

for i in range(dievu_sk):
    olimpo_dievai[i].skaiciavimas()

for i in range(dievu_sk):
    olimpo_dievai[i].print_data()
