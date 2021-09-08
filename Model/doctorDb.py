import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abruabru66",
    port = '3306',
    database = 'pms'
)
myCursor = db.cursor()
myCursor.execute("INSERT INTO `pms`.`doctor` (`doctorId`, `Name`, `qualification`, `inst`, `speciality`) VALUES ('111', 'Dr. Peter Parker', 'MBBS, MD', 'Harvard Medical School', 'ENT')")
db.commit()

myCursor.execute("SELECT * from doctor")
doctor = myCursor.fetchall()
print(doctor)