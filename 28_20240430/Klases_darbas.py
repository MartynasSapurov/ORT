my_pets = ['alfred', 'tabitha', 'william', 'arla']

#pritaikę map funkciją sukurkite naują sąrašą kuriame bus tik pirmosios trys vardų vaidės

my_upper_pets_4 = list(map(lambda x: [x[0].upper(), x[1].upper()], my_pets))

print(my_upper_pets_4)

#Pakeiskite lambda funkciją, paprasta funkcija
