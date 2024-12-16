with open("U1.txt", 'rt') as kombinatorika:
    zaideju_skaicius = int(kombinatorika.readline())
    duomenys = [[int(item) for item in line.split()] for line in kombinatorika.readlines()]
    #duomenys = []
    #for i in range(zaideju_skaicius):
    #    duomenys.append([int(item) for item in kombinatorika.readline().split()])

zaideju_numeriai = {item[0]: [0, 0, 0, 0, 0] for item in duomenys}

for zaidejas in zaideju_numeriai:
    for item in duomenys:
        if zaidejas == item[0]:
            zaideju_numeriai[zaidejas][0] += 1

daugiausia_rungtyniu = max([item[0] for item in zaideju_numeriai.values()])

daugiausiai_zaide = {}

zaideju_numeriai = {index: value for index, value in zaideju_numeriai.items() if value[0] == daugiausia_rungtyniu}
"""
for index, value in zaideju_numeriai.items():
    if value[0] == daugiausia_rungtyniu:
        daugiausiai_zaide[index] = value
print(daugiausiai_zaide)
"""

for zaidejas in zaideju_numeriai:
    #print(zaidejas, zaideju_numeriai[zaidejas])
    for item in duomenys:
        if zaidejas == item[0]:
            #print(item)
            zaideju_numeriai[zaidejas][1] += item[1]+(item[3]*2)+(item[5]*3)
            zaideju_numeriai[zaidejas][2] += item[1]+item[3]+item[5]
            zaideju_numeriai[zaidejas][3] += item[2]+item[4]+item[6]
            #zaideju_numeriai[zaidejas][1] += item[1]
            #zaideju_numeriai[zaidejas][2] += item[3]
            #zaideju_numeriai[zaidejas][3] += item[5]

for zaidejas in zaideju_numeriai:
    zaideju_numeriai[zaidejas][1] = round(zaideju_numeriai[zaidejas][1] / daugiausia_rungtyniu, 1)
    zaideju_numeriai[zaidejas][4] = int(round(100*zaideju_numeriai[zaidejas][2]/zaideju_numeriai[zaidejas][3], 0))
    #zaideju_numeriai[zaidejas][1]=round(zaideju_numeriai[zaidejas][1]/daugiausia_rungtyniu, 1)
    #zaideju_numeriai[zaidejas][2] = round(zaideju_numeriai[zaidejas][2] / daugiausia_rungtyniu, 1)
    #zaideju_numeriai[zaidejas][3] = round(zaideju_numeriai[zaidejas][3] / daugiausia_rungtyniu, 1)

with open("Rez1.txt", 'wt') as kombinatorika:
    kombinatorika.write(f"{daugiausia_rungtyniu}\n")
    for zaidejas in zaideju_numeriai:
        kombinatorika.write(f"{zaidejas} {zaideju_numeriai[zaidejas][1]} {zaideju_numeriai[zaidejas][4]} %\n")
#print(daugiausia_rungtyniu)
#print(zaideju_numeriai)
