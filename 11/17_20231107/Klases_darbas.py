# Paklauskite vartotojo amžiaus.
# Jei amžius mažesnis arba lygus 0 arba įvestas ne skaičius - išvesti Wrong input
# Jeigu amžius mažesnis arba lygus 12 - išvesti Bike
# Jeigu amžius didesnis nei 12 ir mažesnis nei 18 - išvesti Scooter
# Kitu atveji - išvesti Car

"""
age = input('Input your age: ')

if not age.isdigit() or int(age) <= 0:
    print('Wrong input')
else:
    age = int(age)
    if age <= 12:
        print('Bike')
    elif age < 18:
        print('Scooter')
    else:
        print('Car')
"""
#Darbas su simboliais ir jų kodavimo sistemos

japan_str = 'ぁぃえおき げず㍿ボ゛' #Japnų simbolių eilutė
japan_char = '㍿' #Japonų simbolis
hebrew_str = "שָׁלוֹם" #Hebrajų simbolių eilutė

color = 'red' #Standartinių ASCII lentelės simbolių eilutė
name = 'Tom' #Standartinių ASCII lentelės simbolių eilutė

cyrillic = 'Арефа' #Rusų (Kirilica) simbolių eilutė

#Spausdinami užkoduoti japoniški rašmenys,
#jeigu nenurodoma jokia kodavimo sistema automatiškai taikoma numatytoji utf-8
#pagrindinių kodavimo sistemų (codecs) sąrašą rasite
#https://docs.python.org/2.3/lib/node130.html

print("*"*40)
print("Japanese characters")
print(japan_str.encode())
print(japan_char.encode())

print("*"*40)
print("Hebrew characters")
print(hebrew_str.encode())

print("*"*40)
print("ASCII characters")
print(color.encode())
print(name.encode())

print("*"*40)
print("Cyrillic characters")
encoded_cyrillic = cyrillic.encode()

print('Original cyrillic text:', cyrillic)
print('Encoded cyrillic text:', encoded_cyrillic)
print('Decoded cyrillic text using wrong codec:', encoded_cyrillic.decode(encoding='Latin1'))

#Teksto perkodavimas iš vienos kodavimo sistemos (codec) į kitą
#artist_utf_8 - utf-8 užkoduotas tekstas baitų (bytes) pavidalu (hex, arba hexadecimal - šešioliktainiai skaiytmenys)
artist_utf_8 = b'Tage \xc3\x85s\xc3\xa9n'

print("*"*40)
print("Encoded text (Utf-8):", artist_utf_8)
print("Data type:", type(artist_utf_8))
print("Data length:", len(artist_utf_8))

#Iškoduotas tekstas
artist = artist_utf_8.decode()
print("Decoded text", artist)
print("Data type:", type(artist))

#Tekstas užkoduotas Utf-32
artist_utf_32 = artist.encode(encoding='utf-32')
print("Encoded text (Utf-32):", artist_utf_32)
print("Data type:", type(artist_utf_32))
print("Data length:", len(artist_utf_32))

#Tekstas užkoduotas Latin1
artist_latin_1 = artist.encode(encoding='Latin1')
print("Encoded text (Latin1):", artist_latin_1)
print("Data type:", type(artist_latin_1))
print("Data length:", len(artist_latin_1))
