with open('U1.txt', 'r') as f:
    duomenys = list(map(int, f.readline().split()))
    #duomenys = [int(item) for item in f.readline().split()]

mokiniai = [0] * 20

"""
mokiniai = [0 for _ in range(20)]

mokiniai = []

for _ in range(20):
    mokiniai.append(0)
"""
for i in range(10):
        mokiniai[i] = 10-duomenys[i]

for i in range(10):
    slyvos = 10 - duomenys[i]
    for j in range(i + 1, 20):
        if slyvos > 0:
            mokiniai[j] += 1
            slyvos -= 1
        else:
            break

print(mokiniai)
