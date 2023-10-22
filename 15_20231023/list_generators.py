my_old_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
my_string = "1,3,5,7,8,10,15,14"
my_new_tuple = tuple(item for item in my_old_tuple)
#my_string_tuple = tuple(item for item in my_string)
my_string_list = []

my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}

a = 3
b = 4

if a > b:
    max = a
else:
    max = b




#my_string_list = tuple(item for item in my_old_tuple if not (item % 7))
for item in my_old_tuple:
    my_string_list.append(item) if not(item % 7) else item



#my_string_list = [item for item in my_old_tuple[::-1] if not(item % 7)]


print(my_string_list)

"""
print(max)



for item in my_string.split(','):
    my_string_list.append(int(item))

print(my_new_tuple)
print(my_old_tuple)

print(my_string)
print(my_string_list)
"""