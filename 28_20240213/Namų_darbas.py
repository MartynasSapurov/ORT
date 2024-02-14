# Namų darbo užduotis Markui, Doniui ir Airanaui
# Savo sukurtame ir pasidalintame su manimi ir savo porininku GitHub projekte parašykite funkciją kurios įėjimas yra elutė kurią sudaro 6 kableliu atskirtos vertės
# Jūsų funkcija turi prisijungti prie jūsų duomenų bazės su kuriomis dirbome ir į ją įrašyti naują studentą.
# Kai tik atliksite šia užduoti suformuluosiu užduotis jūsų porininkams

# Ši programa prisijungia prie jųsų duomenų bazės ir atspausdina pirmąjį įrašą iš studentų lenetlės

import pymysql

# Prisijungiame prie duomenų bazės
db = pymysql.connect(host='3.121.198.11',  port=3306, user='martynas', password = "martynas", db='martynas')

# paruošiame prisijungimui cursor() methodą
mysql_cursor = db.cursor()

# pasiruošiame užklaus, šiuo atveju nuskaityti duomenis iš lentelės studentai
sql = "SELECT * FROM Studentai"

# Namų darbo užduočiai atlikti reikės naudoti užklausą panašią į
# INSERT INTO `Studentai` VALUES ('11', 'Šapurov', 'Martynas', 'ER-1', '22222222', b'1')

# Įvykdome užklausą ir atspausdiname pirmąją lentelės studentai eilutę
try:
        mysql_cursor.execute(sql)
        print(mysql_cursor.fetchone())
except:
        print ("Error: unable to fecth data")

# atsijungiame nuo serverio
db.close()
