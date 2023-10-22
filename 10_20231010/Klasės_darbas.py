#Pagrindiniai sąrašų tipai Python

#Kortežas (tuple) - nekeičiamas duomenų tipas
my_tuple = (1, 2)

#Sąrašas (list) - keičiamas duomenų tipas
my_list = [1, 2]

#Aibė (set) - keičiamas duomenų tipas
my_entity = {1, 2}

#Žodynas (dictionary) - keičiamas duomenų tipas
my_dictionary = {1: 1, 2: 2}

#Naujo elemento įterpimas į sąrašą
print(my_list)
print(f"Sąrašas my_list saugomas atminties lastelėje {id(my_list)}")
my_list.append(3)
print(my_list)
print(f"Sąrašas my_list saugomas atminties lastelėje {id(my_list)}")

#Naujo elemento įterpimas į sąrašą įvedamas iš klaviatūros
my_list.append(int(input("Įveskite papildomą elemtą ")))
print(my_list)
print(f"Sąrašas my_list saugomas atminties lastelėje {id(my_list)}")
#Adresas visuomet toks pats

#Naujo elemento įterpimas į kortežą
print("*" * 80)
print(my_tuple)
print(f"Kortežas my_list saugomas atminties lastelėje {id(my_tuple)}")
#Tiesiogiai naujo elemto pridėti negalima, todėl atliekama dviejų kortežų suma
my_tuple += (5,)
print(my_tuple)
print(f"Kortežas my_list saugomas atminties lastelėje {id(my_tuple)}")

#Kitas metodas atlikti pakeitimus korteže yra pakeisti jį į sąrašą, atlikti pakeitimus ir pakeisti atgal į kortežą
my_tuple = list(my_tuple)
my_tuple.remove(5)
my_tuple = tuple(my_tuple)

print(my_tuple)
print(f"Kortežas my_list saugomas atminties lastelėje {id(my_tuple)}")

#Atkreipkite dėmesį, kad kiekvieną kartą gaunamas kitas atminties adresas

"""
Susipažinkite ir savarankiškai išbandykite sąrašų metodus:

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

Susipažinkite ir savarankiškai išbandykite kortežų metodus:
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""