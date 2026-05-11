#1. Užduotis
#Parašykite programą kuri perskaitytų duomenis iš failo "file0.txt" ir išvestu po vieną eilutę
"""
with open("file0.txt", mode="r", encoding="utf8") as file:
    data = [item[:-1] for item in file.readlines()]
    #print(data)
    for item in data:
        print(item)
"""

#2. Užduotis
#Parašykite programą kuri suskaičiuotų kiek faile "file1.txt" yra eilučių neprasidedančių raide "T".
"""
with open("file1.txt", mode="r", encoding="utf8") as file:
    data = [item[:-1] for item in file.readlines()]
    n = 0
    for item in data:
        if len(item) > 0:
            if item[0] != "T":
                n+=1
print(n)
"""

#3. Užduotis
#Parašykite programą kuri suskaičiuotų kiek faile "file1.txt" yra žodžių
"""
with open("file1.txt", mode="r", encoding="utf8") as file:
    data = file.read().split()
    print(len(data))
"""
#4. Užduotis
#Parašykite programą kuri suskaičiuotų kiek kartų faile "file1.txt" yra minimas žodis "the" arba "The".
"""
with open("file1.txt", mode="r", encoding="utf8") as file:
    data = [item.capitalize() for item in file.read().split()]
    #data = list(map(lambda x: x.lower(), file.read().split()))
    n=0
    for item in data:
        if item == "The":
            n+=1
print(n)
"""

#5. Užduotis
#Parašykite programą kuri suskaičiuotų kiek faile "file1.txt" yra žodžių trumpesnių nei 4 simboliai
"""
with open("file1.txt", mode="r", encoding="utf8") as file:
    data = file.read().split()
    n=0
    for item in data:
        if len(item) < 4:
            n+=1
print(n)
"""

#6. Užduotis
#parašykite programą kuri suskaičiuotų kiek faile "file2.txt" yra žodžių "this" and "these", atkreipkite dėmesį, kad
#būtų skaičiuojami tik pilni žodžiai
"""
with open("file2.txt", mode="r", encoding="utf8") as file:
    data = file.read()
    ch = ["\"", ",", "."]
    for i in ch:
        data = data.replace(i, "")
    data = [item.lower() for item in data.split()]
    n=0
    for item in data:
        if item == "this" or item == "these":
            n+=1
print(n)
"""
#7. Užduotis
#parašykite programą kuri suskaičiuotų kiek faile "file2.txt" yra žodžių užsibaigiančių raide "e"
"""
with open("file2.txt", mode="r", encoding="utf8") as file:
    data = file.read()
    ch = ["\"", ",", "."]
    for i in ch:
        data = data.replace(i, "")
    data = [item.lower() for item in data.split()]
    n=0
    for item in data:
        if item[-1] == "e":
            n+=1
print(n)
"""
#8. Užduotis
#parašykite programą kuri suskaičiuotų kiek faile "fil2.txt" yra didžiųjų raidžių
"""
with open("file2.txt", mode="r", encoding="utf8") as file:
    data = []
    for item in file.read():
        if item.isalpha():
            if item.isupper():
                data.append(item)
print(len(data))
"""
#9. Užduotis
#parašykite programą kuri nuskaitytų duomenis if "file3.txt" ir ištrintu visus $ ženklus
"""
with open("file3.txt", mode="r", encoding="utf8") as file:
    data = file.read()
    data = data.replace("$", "")

print(data)
"""

#10. Užduotis
#parašykite programą kuri nuskaituytų duomenis iš failo "file4txt" ir nekeičiant failo atspausdintų duomenis
#pakeičiant visus simbolius "xwz" į "h"
"""
with open("file4.txt", mode="r", encoding="utf8") as file:
    data = file.read()
    data = data.replace("xwz", "h")

print(data)
"""
