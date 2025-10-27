#Darbas su simboliais ir jų kodavimo sistemos

japan_str = 'ぁぃえおき げず㍿ボ゛' #Japnų simbolių eilutė
japan_char = '㍿' #Japonų simbolis

hebrew_str = "שָׁלוֹם" #Hebrajų simbolių eilutė
hebrew_char ="ם"

color = 'red' #Standartinių ASCII lentelės simbolių eilutė
name = 'Tom' #Standartinių ASCII lentelės simbolių eilutė

lithuanian = "sūkuriuoja"

cyrillic = 'Борис Стругацкий' #Rusų (Kirilica) simbolių eilutė

#Spausdinami užkoduoti japoniški rašmenys,
#jeigu nenurodoma jokia kodavimo sistema automatiškai taikoma numatytoji utf-8
#pagrindinių kodavimo sistemų (codecs) sąrašą rasite
#https://docs.python.org/2.3/lib/node130.html
"""
print("*"*40)
print(japan_str)
print(japan_str.encode())
print(japan_char.encode())

print("*"*40)
print(hebrew_str)
print(hebrew_str.encode())
print(hebrew_char.encode())

print("*"*40)
print(color)
print(color.encode())

print("*"*40)
print(lithuanian)
print(lithuanian.encode())

print("*" * 40)
print(cyrillic)
print(cyrillic.encode("koi8_r"))
print(cyrillic.encode("utf-8"))
"""
print("*" * 40)
print("Cyrilic characters")

encoded_cyrillic = cyrillic.encode()
print(encoded_cyrillic)
print("*" * 40)
print("Print original text", cyrillic)
print("Encoded cyrillic text", encoded_cyrillic)
print("Decoded using wrong codec", encoded_cyrillic.decode(encoding="latin_1"))

#Teksto perkodavimas iš vienos kodavimo sistemos (codec) į kitą
#artist_utf_8 - utf-8 užkoduotas tekstas baitų (bytes) pavidalu (hex, arba hexadecimal - šešioliktainiai skaiytmenys)
artist_utf_8 = b'Tage \xc3\x85s\xc3\xa9n'
print("*" * 40)
print("Artist encoded text", artist_utf_8)
print("Data type", type(artist_utf_8))
print("Data lenght", len(artist_utf_8))

#Iškoduotas tekstas
artist = artist_utf_8.decode()
print("Decoded text", artist)
print("Data type", type(artist))

#Tekstas užkoduotas Utf-32
artist_utf_32 = artist.encode(encoding='utf-32')
print("Artist encoded text", artist_utf_32)
print("Data type", type(artist_utf_32))
print("Data lenght", len(artist_utf_32))

#Tekstas užkoduotas Latin1
artist_latin_1 = artist.encode(encoding='Latin1')
print("Encoded text (Latin1):", artist_latin_1)
print("Data type:", type(artist_latin_1))
print("Data length:", len(artist_latin_1))
