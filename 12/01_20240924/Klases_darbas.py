"""
my_list = ['pirmas', 'antras', 'trecias', 'ketvirtas', 'ketvirtas']
my_tuple = ('pirmas', 'antras', 'trecias', 'ketvirtas', 'ketvirtas')
my_set = {'pirmas', 'antras', 'trecias', 'ketvirtas'}
my_dict = {1:'pirmas', 2:'antras', 'geriausias_skaicius':'trecias', 4:'ketvirtas'}

print(f"List is: {my_list} \nType is: {type(my_list)}")
print("*"*80)
print(my_tuple, type(my_tuple), sep='\n')
print("*"*80)
print(my_set, type(my_set), sep='\n')
print("*"*80)
print(my_dict, type(my_dict), sep='\n')
print("*"*80)
print(my_dict['geriausias_skaicius'])
"""
"""
file = open('U1.txt', 'rt')
my_line = file.readline()
file.close()

print(my_line)

with open('U1.txt', 'rt') as file:
    my_line = file.readline()

print(my_line)

try:
    file = open('U1.txt', 'rt')
    my_line = file.readline()
finally:
    file.close()

print(my_line)
"""
"""
#my_list = []
with open('U1.txt', 'rt') as file:
    n = int(file.readline())
    my_list = file.readline().split()
    my_list = [int(item) for item in my_list]
    print(my_list)
"""

"""
my_new_list = []

my_other_list = [1, 5, 7, 8]

my_new_list.append(my_other_list)
my_other_list = [8, 7, 5, 1]
my_new_list.append(my_other_list)
print(my_new_list[0][1], my_new_list[1][1], sep="\n")
"""
"""
my_list = []
with open('U1.txt', 'rt') as file:
    n = int(file.readline())
    for item in range(n):
        my_list.append([int(x) for x in(file.readline().split())])

    print(my_list)
"""

"""
for item in range(n):
    print(f"Žaidėjo numeris: {my_list[item][0]}, jis pataikė: {my_list[item][1]} baudinių, {my_list[item][3]}"
          f" dvitaškių ir {my_list[item][3]} tritaškių")
"""


with open('U1.txt', 'rt') as file:
    my_list = [[int(item) for item in items.split()] for items in file.readlines()[1:]]
    print(my_list)
    #my_list = file.readline().split()
    #my_list = [int(item) for item in my_list]
    #print(my_list)

"""
line = []
with open('U1.txt', 'rt') as file:
    n=int(file.readline())
    print(n)
    for i in range(n):
        line.append([int(item) for item in file.readline().split()])
    print(line)
"""
