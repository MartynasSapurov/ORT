"""
my_list = input().split()
print(my_list)

my_new_list = list(map(int, my_list))

print(my_new_list)
"""
def keitimas(x):
    x = str(x)[0]+"6"
    return int(x)



my_list = [40, 50, 60, 70, 80, 90, 100]

"""
sum = ""

my_list = list(map(str, my_list))


for item in my_list:
    sum += item

print(sum)
"""
my_list = list(map(keitimas, my_list))

print(my_list)

"""
Patobulinkite funkcija, kad visi sąraši skaičių "0" būtų keičiami į "6"
"""
