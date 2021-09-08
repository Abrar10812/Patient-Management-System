import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abruabru66",
    port = '3306',
    database = 'pms'
)
myCursor = db.cursor()