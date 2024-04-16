my_pets = ['alfred', 'tabitha', 'william', 'arla']

#pritaikę map funkciją sukurkite naują sąrašą kuriame bus tik pirmosios trys vardų vaidės

def my_fumc(x):
  return x.upper()

my_newlist[]

my_newlist = list(map(my_fumc, my_pets))

#Duotas sąrašas taškų (skaičių)
#pritaikę map() funkciją sukurkite naują sąrašą
#kuriame pirmasis elementas turės 1 skaičių po kalbelio, antras 2 ir tt.

circle_areas = [3.567738, 5.576681, 4.009147, 56.242413, 9.013442, 32.000133]
new_areas = list(map(round, circle_areas, [i for i in range(1, len(circle_areas)+1)]))
print(new_areas)
