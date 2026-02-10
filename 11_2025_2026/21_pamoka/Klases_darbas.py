komplektai = [8, 2, 2, 2, 1, 1]
figuros = [0, 0, 0, 0, 0, 0]

with open('U1.txt', 'r') as file:
    n = int(file.readline())
    for _ in range(n):
        mokinio_figiros = list(map(int, file.readline().strip().split()))
        for i in range(len(mokinio_figiros)):
            figuros[i]+=mokinio_figiros[i]

print(figuros)

for i in range(len(mokinio_figiros)):
    komplektai[i] = figuros[i]//komplektai[i]

print(min(komplektai))
