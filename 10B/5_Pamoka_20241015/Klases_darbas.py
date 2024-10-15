#Parašykite programšykite programą kuri paprašytų iš pradžių įvesti jūsų vardą po to amžių.
#Patikrinkite ar įvestas amžius yra skaičius (age.isdigit())
#Jeigu ne parašykite įvesti netinkami duomenys
#tada patikrinkite ar amžius nelygus 0, jeigu lygus parašykite įvesti netinkami duomenys
#Jei amžius didesnis už 0 ir mažesnis už 10 parašykite "Labas jaunikaiti "Vardas""
#Jei amžius didesnis arba lygus 10 ir mažesnis arba lygus 18 parašykite "Kaip sekasi "Vardas""
#Jei amžius didesnis už 18 ir mažesnis nei 100 paraškite "Ko peigeidaujate "Vardas""
#Visais kiatis atvejais parašykite ""Vardas" jūs meluojate, jums negali būti tiek metų"

Sprendimas
name = input("Įveskite savo vardą\n")
age = input("Įveskite skaičių\n")
if not age.isdigit():
    print("Įvesti netinkami duomenys")
elif int(age) == 0:
    print("Įvesti netinkami duomenys")
elif int(age) < 10:
    print(f"Labas jaunikaiti {name}")
elif int(age) <= 18:
    print(f"Kaip sekasi {name}")
elif int(age) <100:
    print(f"Ko peigeidaujate {age}")
else:
    print(f"{age} jūs meluojate, jums negali būti tiek metų")
