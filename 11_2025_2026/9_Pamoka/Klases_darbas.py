#File open
file = open('failas_Kajaus.txt', 'w')
file.write("Labas\nKą tu dabar darai?\nIki")
file.close()

print(40*"*")
"""
with open('failas_Kajaus.txt', 'r') as file:
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')
"""
with open('failas_Kajaus.txt', 'r') as file:
    print(file.readlines())

print(40*"*")
#Try file open konstruktorius
try:
    file = open('failas_Kajaus.txt')
    a = file.read()
    print(a)
    print(type(a))
finally:
    file.close()

duomenys = []
with open('Data.txt', 'r') as file:
    n = int(file.readline())
    for _ in range(n):
        duomenys.append([int(item) for item in file.readline().split()])

print(duomenys)

#Savarankiška užduotis
#Atspausdinkite 4 pirmojo nario elementą
#Atspausdinkite kas antrą antrojo nario elementą atvikščiai
#Pakelkite kvadratu kas antrą 3 nario elemntą
#Atspausdinkite pirmajį ir paskutinį 4 ketvirto nario elementus
