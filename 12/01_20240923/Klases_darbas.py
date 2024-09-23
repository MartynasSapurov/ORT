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
#my_list = []
with open('U1.txt', 'rt') as file:
    n = int(file.readline())
    my_list = file.readline().split()
    my_list = [int(item) for item in my_list]
    print(my_list)

my_new_list = []

my_other_list = [1, 5, 7, 8]

my_new_list.append(my_other_list)
my_other_list = [8, 7, 5, 1]
my_new_list.append(my_other_list)
print(my_new_list[0][1], my_new_list[1][1], sep="\n")
