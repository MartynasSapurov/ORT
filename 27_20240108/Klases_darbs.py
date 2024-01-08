with open('test.txt', 'rt') as file:
    my_list = file.readlines()

my_string = ''
for item in my_list:
    my_string += item[:-1]+" "

my_new_list = my_string.split()

print(my_new_list)
