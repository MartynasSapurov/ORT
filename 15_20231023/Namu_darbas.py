#Duotas žodynas, sukurkite naują žodyną jo pagrindu pasitelkdami sąrašų (žodynų) generatorių
chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}
"""
1. Naujajame žodyne sukesikite indeksus ir vertes vietomis
2. Į naująjį žodyną įtraukite tik tuos įrašus kurių vertės originaliame žodyne didesnės nei 2000
3. Naujojo žodyno vertės turi susidėti ne iš pavardės ir vardo, atskirtų kalbleliais, o iš pavardės ir pirmosios vardo raidės.

Rezultatas pasitikrinimui:
{
    2804: 'Firouzja A.', 
    2799: 'Ding L.', 
    2773: 'Nepomniachtchi I.'
}
"""

best_players = {value: f"{item.split()[0][:-1]} {item.split()[1][0]}." for item, value in chess_players.items() if value > 2000}

print(chess_players)
print(best_players)
