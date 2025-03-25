"""
n = int(input("Įveskite skaičių "))

for i in range(1, n+1, 2):
    print(i, end=", ")

for i in range(2, n+1, 2):
    print(i, end=", ")
"""
suma = 0
n = int(input("Įveskite skaičių "))
k = 1
for i in range(1, n+1):
    suma+=i*k
    k+=2

print(suma)
