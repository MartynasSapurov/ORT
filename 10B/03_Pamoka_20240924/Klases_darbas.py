"""
1. Sraigė per valandą nušliaužia z žiogo šuolių. Žiogas vienu šuoliu nušoka c centimetrų. Kiek centimetrų
sraigė nušliauš per v valandų? Parašykite programą šiam uždaviniui spręsti.
Pasitikrinkite. Kai z = 2, c = 2, v = 8, tai turi būti spausdinama 32.
"""
z = int(input("Įveskite žiogo šuolių kiekį:\n")) #Nuskaitome žiogo šuolių kiekį
c = int(input("Įveskite žiogo šuolių ilgį, cm:\n")) #Nuskaitome žiogo šuolio ilgį cm
v = int(input("Įveskite kiek valandų šliauš sraigė:\n")) #Nuskaitome kiek valandų šliauš sraigė

result = z*c*v

print(f"Sraigė nušliauš {result} cm")

"""
2. Laivynas iš k laivų, kurių kiekvienas plukdė po n maišų prieskonių, pakliuvo į audrą, kurioje m laivų
nuskendo, o kiti sėkmingai pasiekė kelionės tikslą. Kiek maišų prieskonių pavyko parvežti?
Pasitikrinkite. Kai k = 15, n = 8000 , m = 3, tai pavyko parvežti 96000 maišų prieskonių.

3. Per kiek laiko tamsiame urve paklydęs turistas vieną po kito sudegins n degtukų, jei kiekvienas iš jų dega m
minučių? Atsakymą išreikškite valandomis ir minutėmis.
Pasitikrinkite. Kai n = 75, m = 2 , tai degtukai sudegs per 2 val. ir 30 min.
minutes = 105

valandos = int(minutes/60)
minutes = minutes%60

print(valandos, minutes)

4. Laikrodis rodo x valandų ir y minučių. Parašykite programą, kuri apskaičiuotų, kiek minučių minut ir
kiek sekundžių sec prabėgo nuo vidurnakčio.
Pasitikrinkite. Įvedę x = 3 ir y = 5, turėtumėte gauti: minut = 185, sec = 11100.
"""
