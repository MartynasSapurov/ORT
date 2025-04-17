pradine_kaina = int(input())
zuvu_kiekis = int(input())
kaina = pradine_kaina
for i in range(zuvu_kiekis):
    print(kaina)
    kaina=kaina*pradine_kaina

pirminis = False

if n % i:
    pirminis = True
    
if pirminis == True:
    print("TAIP")
else:
    print("NE")
