ef my_global_sufganiot_1():
    while 1:
        a = input("Įveskite skaičių: ")
        if a.isdigit():
            break

    a = int(a)
    return a


def my_global_sufganiot_2():
    def my_local_sufganiot_1():
        while 1:
            a = input("Įveskite skaičių: ")
            if a.isdigit():
                break

        a = int(a)
        return a

    a = my_local_sufganiot_1()
    b = my_local_sufganiot_1()
    return a, b


my_sufganiot_dict = {"Šuo": "Dog", "Katė": "Cat"}
"""
word = input("Įveskite skaičių du kableliu atskirtus žodžius: ")
a = word.split(', ')[0]
b = word.split(', ')[1]


my_sufganiot_dict[a] = b
"""
print(my_sufganiot_dict)
for item in my_sufganiot_dict.values():
    print(item)
