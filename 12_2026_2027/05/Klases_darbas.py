class basketball(object):
    def __init__(self, zaidejo_numeris, pat_1=0, mest_1=0, pat_2=0, mest_2=0, pat_3=0, mest_3=0, suzaista_rungt=0):
        self.zaidejo_numeris=zaidejo_numeris
        self.pat_1=pat_1
        self.mest_1=mest_1
        self.pat_2=pat_2
        self.mest_2=mest_2
        self.pat_3=pat_3
        self.mest_3=mest_3
        self.suzaista_rungt=suzaista_rungt

    def statistikos_papildymas(self, metimai):
        self.pat_1+=metimai[0]
        self.mest_1+=metimai[1]
        self.pat_2+=metimai[2]
        self.mest_2+=metimai[3]
        self.pat_3+=metimai[4]
        self.mest_3+=metimai[5]
        self.suzaista_rungt+=1

    def spausdinimas(self):
        print(f"zaidejo_numeris={self.zaidejo_numeris}, suzaista_rungt={self.suzaista_rungt}, pat_1={self.pat_1}, mest_1={self.mest_1}, pat_2={self.pat_2}, mest_2={self.mest_2}, pat_3={self.pat_3}, mest_3={self.mest_3}")

with open("U1.txt") as file:
    zaideju_sk = int(file.readline())
    print(zaideju_sk)
    my_list=[]
    for i in range(zaideju_sk):
        line = list(map(int, file.readline()[:-1].split()))
        my_list.append(line)


zaideju_numeriai = {item[0] for item in my_list}

staistika = []

for item in zaideju_numeriai:
    staistika.append(basketball(item))

for i in range(len(staistika)):
    for item in my_list:
        if staistika[i].zaidejo_numeris==item[0]:
            staistika[i].statistikos_papildymas(item[1:])

print(my_list)

for item in staistika:
    item.spausdinimas()

