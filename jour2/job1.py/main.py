import mysql.connector

datab = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Freefight7.",
    database = "LaPlateforme"

)

cursor = datab.cursor()

cursor.execute("SELECT * FROM etudiants")

resultat = cursor.fetchall()

print (resultat)

datab.close()