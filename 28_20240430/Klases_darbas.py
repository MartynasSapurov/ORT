#1
my_pets = ['alfred', 'tabitha', 'william', 'arla']

#pritaikę map funkciją sukurkite naują sąrašą kuriame bus tik pirmosios trys vardų vaidės

my_upper_pets_4 = list(map(lambda my_pets: my_pets[:3].upper(), my_pets))

print(my_upper_pets_4)

#Pakeiskite lambda funkciją, paprasta funkcija


#2
#################################################################################

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]


def my_func(x):
    return x > 75

answer = list(filter(my_func, scores))

print(answer)

#Namuose parašykite su lambda funkcija
#3
#Taikydami map funkcija vardus saraše prasidedančius raide "a" pakeiskite visomis didžiosiomis raidėmis, o visus kitus užrašykite atbulai.

my_pets = ['alfred', 'tabitha', 'william', 'arla']
