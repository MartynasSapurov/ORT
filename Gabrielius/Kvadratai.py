pi = 355/113

def plotai(a):
    ibreztas = pi*(a/2)**2
    apibreztas = pi*a**2/2
    return ibreztas, apibreztas

def isvestis(plotai):
    print(f"Įbrėžto plotas: {plotai[0]:.2f}\nApibrėžto plotas: {plotai[1]:.2f}")
    return 0

a = int(input("Įveskite lvadrato kraštinę\n"))

isvestis(plotai(a))
