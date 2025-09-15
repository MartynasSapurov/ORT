
#Įvairūs sąrašai

#Koertežas (tuple)
print("-"*40)
my_tuple = ("Petras", "Jonas", "Aaronas", "Gabrielius")
print(f"Sio saraso tipas – {type(my_tuple)}")
for item in my_tuple:
    print(item)

#Sąrašas (list)
print("-"*40)
my_list = ["Petras", "Jonas", "Aaronas", "Gabrielius"]
print(f"Sio saraso tipas – {type(my_list)}")
for item in my_list:
    print(item)

#Aibė (set)
print("-"*40)
my_set = {"Petras", "Jonas", "Aaronas", "Gabrielius"}
print(f"Sio saraso tipas – {type(my_set)}")
for item in my_set:
    print(item)

#Žodynas (dictionary), atkreipkite dėmesį, kad kiekvieną kartą įrašai išvedami vis kita tavarka, paeksperimentuokite
print("-"*40)
my_dictionary = {"Petras":"Eimaontas", "Jonas":"Kazlauskas", "Aaronas":"Perednis", "Gabrielius":"Brazdeikis"}
print(f"Sio saraso tipas – {type(my_dictionary)}")
for item in my_dictionary:
    print(f"{item} {my_dictionary[item]}")

#For ciklas ir itertaotriai, svarbu suprasti, kad for ciklas iš eilės praina visas iteratoruojmas reikšmes
print("#"*40)

my_tuple = ("Pirmas", "Antras", "Trecias", "Ketvirtas")
print("Saraso elementai")
for item in my_tuple:
    print(item)

print("#"*40)
print("Saraso elementai taikant range funkcija")
my_len = len(my_tuple)
print(f"Lenght is {my_len}")
for i in range(my_len):
    print(my_tuple[i])
