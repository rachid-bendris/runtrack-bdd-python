import mysql.connector

datab = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Freefight7.",
  database="Laplateforme"
)

cursor = datab.cursor()

cursor.execute("SELECT nom, capacite FROM salles")

result = cursor.fetchall()

print(result)

datab.close()