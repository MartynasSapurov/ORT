#Darbas su csv (comma-separated value)
import csv

name_of_fields = ["Eil, nr", "Vardas", "Batų dydis", "Amžius", "Pištų kiekis"]
line_1 = [1, "Kajus", 43, 18, 20]
line_2 = [2, "Austėja", 40, 17, 20]
line_3 = [3, "Budnikas", 44, 17, 19.5]
line_4 = [4, "Golod", 42, 18, 19.99]

#Duomenų įrašymas
with open("11AB.csv", mode="w", encoding="utf8", newline="") as AB11_csvfile:
    file_writer = csv.writer(AB11_csvfile)
    file_writer.writerow(name_of_fields)
    file_writer.writerow(line_1)
    file_writer.writerow(line_2)
    file_writer.writerow(line_3)
    file_writer.writerow(line_4)

#Duomenų nuskaitymas
with open("11AB.csv", mode="r", encoding="utf8", newline="") as AB11_csvfile:
    file_reader = csv.reader(AB11_csvfile)
    for item in file_reader:
        print(item)

#Pasitelkę for cikl1 sugeneruokite atsitiknius duomenis apie 8 klasiokus ir 5ra6ykite CSV formatu
