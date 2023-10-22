#Darbas su sąrašais
letters = ["a", "b", "c", "d", "a"]

print(letters)
print(f"Sąrašas letters saugomas atminties lastelėje {id(letters)}")

#Naujo elemento pridėjimas
letters.append("H")
print(letters)
print(f"Sąrašas letters saugomas atminties lastelėje {id(letters)}")

#Elemento pakeitimas tam tikru indeksu
letters[2] = "A"
print(letters)
print(f"Sąrašas letters saugomas atminties lastelėje {id(letters)}")

#Keliių elementų pakeitimas nurodant intervalą, vertės pateikiamos per ","
letters[0:3] = "H", "a", "s"
print(letters)
print(f"Sąrašas letters saugomas atminties lastelėje {id(letters)}")

#Darbas su aibėmis
my_set = {"a", "b", "c"}
print(my_set)
print(f"Aibė my_set saugomas atminties lastelėje {id(my_set)}")

#Naujo elemento įterpimas į aibę
my_set.update("H")
print(my_set)
print(f"Aibė my_set saugomas atminties lastelėje {id(my_set)}")

print("*"*40)

name = "Martynas"
age = 39


#Spausdinimo funkcija ir eilutės (string) metodai
name = "Martynas"
age = 39

print(f"My name is {name}, I am {age} years old")
print("My name is %s, I am %d years old" % (name, age))
print("My name is ", name, ", I am ", age, " years old", sep="")
print("My name is "+name+", I am "+str(age)+" years old")
print("My name is {}, I am {} years old".format(name, age))

"""
Pasikartokite eilutės (string) metodus ir savarankiškai išbandykite bent du metodus

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""