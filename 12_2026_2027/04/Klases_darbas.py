class shule(object):
    def __init__(self, mokiniai):     
        self.vardas=mokiniai[0]
        self.klase=mokiniai[1]
        self.uniforma=mokiniai[2]


moksleivi_sk=9
moksleiviai_list= [["Kornejus", "12A", True], ["Bernardas", "12B", False], ["Emil", "12B", True], ["Daniel Gus", "12A", False], ["Augustas", "12B", True], ["Danielius Bud", "12A", False],
["Natan", "12A", False], ["Daniel Gol", "12B", True], ["Marta", "12B", False], ["Austeja", "12A", False]]

print(moksleiviai_list[-1])



mokiniai = [shule(moksleiviai_list[i]) for i in range(moksleivi_sk)]
"""
for i in range(moksleivi_sk)):
    mokiniai.append(shule(moksleiviai_list[i]))
"""
print(mokiniai[0].vardas)
