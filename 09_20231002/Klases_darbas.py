#3 Uzd.
#Parašykite programą, kuri nustatytų, ar duotas skaičius n yra pirminis (turi tik du daliklius: vienetą ir patį save).
#Pasitikrinkite. Jei n = 7 , tai atsakymas: 7 yra pirminis. Jei n = 15 , tai atsakymas: 15 yra sudetinis

print("Iveskite skaiciu")
sk = int(input())
count = 0
for i in range(1, sk+1):
    if not(sk % i):
        count = count + 1

if count > 2:
    print(f"{sk} yra sudetinis")
else:
    print(f"{sk} yra pirminis")

#4 Uzd.
"""
Miške auga medžiai, kuriuose bitės kuria savo avilius. Meškiukas žino, jog kur aviliai – ten ir medus. Viena bėda –
aviliai dažnai kabo aukštai, o kopdamas meškiukas devynis prakaitus išlieja. Užkopdamas ar nusileisdamas 1 metrą
meškiukas numeta 1 kilogramą svorio. Tačiau pasiekęs avilį, jis priauga tiek svorio,kiek suvalgo medaus. O suvalgo
tiek medaus, kiek tik randa. Meškiukas žino, kaip aukštai kabo avilys ir kiek kilogramų medaus jame yra. Parašykite
programą, kuri suskaičiuotų, kiek daugiausiai meškiukas gali sverti po pasivaikščiojimo miške. Pirmiausia reikia
įvesti sveikąjį skaičių s – meškiuko dabartinis svorį kilogramais, paskui – medžių su aviliais skaičių miške n, o tada
– skaičius poras, kurios aprašo konkretų medį: pirmasis skaičius reiškia avilio aukštį medyje, antrasis – medaus
kiekį tame avilyje. Net jei avilio aukštis 1, meškiukui teks kopti ir leistis 1 metrą.

Pasitikrinkite. Jei s = 100, n = 5, o skaičiai aprašantys medžius yra tokie: 9 ir 16; 7 ir 15; 5 ir 14; 6 ir 12; 2 ir 10, tai
atsakymas: 109 kg
"""
a, b = input().split(',')
print(a)
print(b)

s = int(input("Iveskite s: "))
n = int(input("Iveskite n: "))

for i in range(1, n+1):
    print("Iveskite", i , "medzio duomenys per ' ir ' zodi: ")
    a, b = input().split("ir")
    s = (s - (int(a) * 2)) + int(b)
    a = 0
    b = 0

print(s,"Kg" )
