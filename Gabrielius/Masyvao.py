my_list = ["Dominykas", "Gabrielius", "Martynas", "Dominykas", ["Ignas", "Danielius", "Robertas"]]

print(my_list)

my_list.append("Lėja")

print("*"*40)
print(my_list)
print("*"*40)


for item in my_list:
    print(f"Sąrašo elementas {item}")

print(len(my_list))

for i in range(len(my_list)):
    print(my_list[i])

print("*"*40)

print(my_list[3])
print("*"*40)

my_dict = {"dog": "šuo", "cat": "katė", "pigeon": "balandis"}

print(my_dict["cat"])
print("*"*40)

for item in my_dict.keys():
    print(item, end=" ")
    print(my_dict[item])

print("*"*40)

for key, value in my_dict.items():
    print(f"{key} = {value}")

#my_set = {"Jonas","Petras"}
#my_set = set(my_list)
#print(my_set)
print("*"*40)

print(my_list[4][1][:2])
