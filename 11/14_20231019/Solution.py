n = int(input())

m = 1
x = 0
while n >= m:
    x += 1
    n = n - m
    if not (x % 2):
        m += 1

print(n, x)
