#Duota simbolių eilutė, kiekvienas atlikte visu variantus:

a = b'\xc5\xa0ven\xc4\x8dion\xc4\x97li\xc5\xb3'
b = b'\xc5\xa0e\xc5\xa1iasde\xc5\xa1imt\xc4\x85j\xc4\xaf'
c = b'D\xc5\xabk\xc5\xa1t\xc5\xb3 \xc4\x85\xc5\xbeuolynas'
d = b'\xc5\xbdvirg\xc5\xbed\xc5\xb3 e\xc5\xbeeras'
e = b'S\xc4\x85\xc5\xa1lav\xc5\xb3 s\xc4\x85\xc5\xa1lavynas'
f = b'\xc5\xbdie\xc5\xbeirb\xc5\xb3 s\xc4\x85ranka'

utf = [a, b, c, d, e, f]
#str_ = []

#Iškoduokite šią eilute taikydami numatytąją kodavimo sistemą (codec)
#Tuomet gautą rezultatą užkoduokite taikydami Latin4 kodavimo sistemą (codec)
#Palyginkite pradinės Utf-8 užkoduotos simbolių eilutės ilgį su naujai užkoduotos simbolių eilutės ilgiu
#Visus rezultatus atspausdinkite


"""
a_str = a.decode()
a_latin = a_str.encode('Latin4')
print(a, len(a))
print(a_str, len(a_str))
print(a_latin, len(a_latin))
"""

#Taikydami sąrašų generatorių užpildykite sąrašą str
print(utf)
str_ = [item.decode() for item in utf]
print(str_)
#Taikydami sąrašų generatorių užpildykite žodyną, latin_dict, kuriame raktas yra kodo ilgis, o vertė kodas Latin4
