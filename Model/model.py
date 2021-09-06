import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abruabru66"
)
myCursor = db.cursor()

myCursor.execute("CREATE DATABASE pms")