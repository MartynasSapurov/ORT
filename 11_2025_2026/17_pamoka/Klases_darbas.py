"""
my_list = [5.012345, 1125.125460, 45.458596]
tinkslumas = [1, 1, 1]
print(my_list)

print(list(map(round, my_list, tinkslumas)))
"""

def over_75(x):
    return x > 75

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]

#print(list(filter(over_75, scores)))
"""
a = int(input())
b = over_75(a)

print(b)

"""
print(list(filter(lambda x: x > 75, scores)))

c = lambda x: x > 75

print(c(85))

"""
Taikydami lambda funkcija išrinkite iš sąrašo my_list tik simetriškus skaišius
"""

my_list = [121, 122, 12321, 15551, 174, 5885, 456]
