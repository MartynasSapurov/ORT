#Paprasčiausi for ciklai
#range(start, stop, step)
ribos = range(1, 21)

for i in ribos:
    if (i % 2) == 0:
        print(f"Skaičius {i} yra lyginis")
    else:
        print(f"Skaičius {i} yra nelyginis")

#1. Atspausdinkite n snaigių.

#Įvedimas
#Natūralus skaičius n (1 ≤ n ≤ 100).
#Išvestis
#Išveskite snaiges skirtingose eilutėse.
#Pasitikrinimui n = 5
"""
*
*
*
*
*
"""

n = int(input("Įveskite snaigių skaičių: "))
print(n)

ribos = range(n)

for i in ribos:
    print("*")
    
#2. Marse savaitę sudaro n dienų. Lyginėmis savaitės dienomis sninga, nelyginėmis - šlapdriba. Atspausdinkite savaitės orų tendenciją.

#Įvedimas
#Natūralus skaičius n (1 ≤ n ≤ 100).
#Išvestis
#Jei sninga - **, jei šlapdriba - *0.
#Pavyzdys
#n = 5
#*0
#**
#*0
#**
#*0
