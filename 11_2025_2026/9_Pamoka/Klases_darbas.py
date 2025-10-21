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

with open('failas_Kajaus.txt', 'r') as file:
    n = int(file.readline())
