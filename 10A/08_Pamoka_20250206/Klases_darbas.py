#10 kartų nuskaitykite klaviatūra įvedamą sveikąjį skaičių, atsakyme patskirai pateikite lyginių ir nelyginių skaičių sumas

suma_lyginiu=0
suma_nelyginiu=0

for _ in range(10):
    skaicius=int(input("Įveskite sveikąjį skaičių\n"))
    if skaicius % 2:
        suma_nelyginiu += skaicius
    else:
        suma_lyginiu += skaicius

print(f"Lyginių skaičių suma {suma_lyginiu}, o nelyginių skaičių suma {suma_nelyginiu}")
