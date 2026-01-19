eluciu_ilgiai = []
ilgiausia_eiute = 0
didziausias_ilgis = 0

with open('Data.txt', 'r') as file:
    data = file.read().split("\n")

for i in range(len(data)):
    raides_eilueje = 0
    for item in data[i]:
        if item.isalpha():
            raides_eilueje+=1
    eluciu_ilgiai.append(raides_eilueje) # įrašome kiekvienos eilutes ilgį į sąrašą


"""
for i in range(len(eluciu_ilgiai)):
    if eluciu_ilgiai[i] > ilgiausia_eilute[1]:
        ilgiausia_eilute[1] = eluciu_ilgiai[i]
        ilgiausia_eilute[0] = i
"""
didziausias_ilgis = max(eluciu_ilgiai)

for i in range(len(eluciu_ilgiai)):
    if eluciu_ilgiai[i] == didziausias_ilgis:
        ilgiausia_eiute = i

print(ilgiausia_eiute+1)



