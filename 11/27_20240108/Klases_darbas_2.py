with open('data.txt', 'rt') as file:
    data_string = file.read()

my_list = tuple(int(i) for i in data_string.split()[:-1])

print(type(my_list))
print(my_list)

print(my_list[0]+my_list[1])
