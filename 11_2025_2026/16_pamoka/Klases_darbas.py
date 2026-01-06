"""
my_list = input().split()
print(my_list)

my_new_list = list(map(int, my_list))

print(my_new_list)
"""
"""
def keitimas(x):
    x = list(str(x))
    for i in range(len(x)):
        if x[i] == '0':
            x[i] = '6'
    return int("".join(x))
"""
def keitimas(x):
    x = str(x).replace('0', '6')

    return int(x)



my_list = [40, 50, 60, 70, 80, 90, 100, 110, 107, 75]

"""
sum = ""

my_list = list(map(str, my_list))


for item in my_list:
    sum += item

print(sum)
"""
my_list = list(map(keitimas, my_list))

print(my_list)
