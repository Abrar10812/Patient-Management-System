import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abruabru66",
    port = '3306',
    database = 'pms'
)

def doctorList():
    myCursor= db.cursor()
    myCursor.execute("SELECT Name FROM pms.doctor;")
    doctorTuple = myCursor.fetchall()
    return doctorTuple