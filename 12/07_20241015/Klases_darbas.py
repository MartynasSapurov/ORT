#Duotas žodynas
my_dict = {"Pirmas": "Danielius", "Antras": "Adam", "Trecias": "Dina", "Ketvirtas":"Danger", "Penktas":"Donis", "Sestas":"Mark"}
#Parašykite programą kuri sukeistu šio žodyno indeksus su vertėmius vietomis


new_dict = {value: key for key, value in my_dict.items()}

new_dict2 = dict()

for key, value in my_dict.items():
    new_dict2[value] = key


#print(my_dict["Trecias"])
