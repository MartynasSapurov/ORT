#https://en.wikipedia.org/wiki/List_of_emojis

vetical = 7
horizontal = 9

"""
print("\U0001f600")
print("\U0001F340")
"""


for i in range(horizontal):
    print("\U0001f600", end="")
print()

for i in range(vetical-2):
    print("\U0001f600", end="")
    for j in range(horizontal-2):
        print("\U0001F340", end="")
    print("\U0001f600", end="")
    print()

for i in range(horizontal):
    print("\U0001f600", end="")
print()
