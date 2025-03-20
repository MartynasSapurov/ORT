#Seką sudaro tam tikro pavidalo skaičiai: 1*1,   2*3,   3*5,   4*7,   5*9, ...
#Apskaičiuokite pirmųjų n sekos narių sumą.
suma = 0
a = 1
n = int(input("Įveskite skaičių: "))
for i in range(1, n+1):
    suma+=(i*a)
    a+=2
print(suma)
