#Parašykite programšykite programą kuri paprašytų iš pradžių įvesti jūsų vardą po to amžių.
#Patikrinkite ar įvestas amžius yra skaičius (age.isdigit())
#Jeigu ne parašykite "Įvesti netinkami duomenys"
#tada patikrinkite ar amžius nelygus 0, jeigu lygus parašykite "Įvesti netinkami duomenys"
#Jei amžius didesnis už 0 ir mažesnis už 10 parašykite "Labas jaunikaiti {Vardas}"
#Jei amžius didesnis arba lygus 10 ir mažesnis arba lygus 18 parašykite "Kaip sekasi {Vardas}"
#Jei amžius didesnis už 18 ir mažesnis nei 100 paraškite "Ko peigeidaujate {Vardas}"
#Visais kiatis atvejais parašykite "{Vardas} jūs meluojate, jums negali būti tiek metų"
a = input("Įveskite skaičių\n")

print(a.isdigit())
