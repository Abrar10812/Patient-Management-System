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

def showDoctorInfo():
    myCursor= db.cursor()
    myCursor.execute("SELECT Name, qualification, speciality FROM pms.doctor;")
    doctorInfo = myCursor.fetchall()
    s = '       '
    n = '\n'
    a = ''
    flag = 1
    for x in doctorInfo:
        a = a + n
        for y in x:
            if flag%3==0:
                a = a + y
            else:
                a= a + y + s
    return a