
"""
my_list={item:19-item for item in range(20)}

sorted(my_list, lambda x )

x = lambda a : a + 10

print(my_list)
"""

with open("U1.txt", "r") as duomenys:
    n = int(duomenys.readline())
    pratimai = {}
    print(n)
    for _ in range(n):
        reiksmes = duomenys.readline().split()
        pratimai[reiksmes[0]] = pratimai.get(reiksmes[0], 0) + int(reiksmes[1])

surusiuotas = sorted(pratimai.items(), key = lambda x: (x[0], -x[1]))

"""
for item in pratimai.items():
    print(item)
"""
print(surusiuotas)
