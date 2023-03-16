import mysql.connector

datab = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Freefight7.",
  database="LaPlateforme"
)

cursor = datab.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

superficie_totale = cursor.fetchone()[0]

print("La superficie de La Plateforme est de", superficie_totale, "m2")

cursor.close()
datab.close()