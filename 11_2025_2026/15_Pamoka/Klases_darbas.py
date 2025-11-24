"""
def smile (a):
    print(a*"\U0001F600")
"""
"""
def dobilas (a):
    print("\U0001F600", end="")
    print(a*"\U0001F340", end="")
    print("\U0001F600")
"""
def dobilas (a):
    print("\U0001F600", end="")
    for i in range(a):
        print("\U0001F340", end="")
    print("\U0001F600")

def smile (a):
    for i in range(a):
        print("\U0001F600", end="")
    print()


smile(9)
for _ in range(5):
    dobilas(7)
smile(9)

a, b, c = [int(item) for item in input().split()]
a, b, c = map(int, input().split())

def klaida():
    print("Blogas pasirinkimas")

def sud(a, b):
    print(f"Sudėtis: {a+b}")

try:
    v, a, b = [int(item) for item in input().split()]
    if v == 1:
        sud(a, b)
    else:
        klaida()

except:
    klaida()

my_list = list(map(int, input().split()))
my_list = [int(item) for item in input().split()]
print(my_list)
