my_dict = {"Vienas": "One", "Du": "Two", "Trys": "Three", "Keturi": "Four", "Penki": "Five",
           "Sesi": "Six", "Septyni": "Seven", "Astuoni": "Eight", "Devyni": "Nine"}
print("*"*40)
print(my_dict)

print("*"*40)
for item in my_dict:
    print(item)

print("*"*40)
for item in my_dict.keys():
    print(item)

print("*"*40)
for key, value in my_dict.items():
    print(key, value)



#Sukeičiame vertes ir indeksus vietomis
my_new_dict = {value: key for key, value in my_dict.items()}
print("*"*40)
print()

print(my_dict)
print(my_new_dict)

