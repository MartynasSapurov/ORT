with open("U1.txt", "r", encoding="utf-8") as duom_failas:
    n = int(duom_failas.readline())
    gimtadienio_sarasas=[]
    for _ in range(n):
        gimtadienio_sarasas.append(list(map(int, duom_failas.readline().split())))
print(gimtadienio_sarasas)

laimeta_pinigu=0
isleista_bilietams=0

for item in gimtadienio_sarasas:
    laimeta_pinigu+=item[0]
    isleista_bilietams+=item[1]

print(laimeta_pinigu)
print(isleista_bilietams)
