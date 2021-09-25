import mysql.connector

class patientDb:


    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Abruabru66",
        port = '3306',
        database = 'pms'
    )
    def newUserSignUp(self, name, phoneNumber, bloodGroup, email, password):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abruabru66",
            port='3306',
            database='pms'
        )
        myCursor = db.cursor(buffered=True)

        myCursor.execute("INSERT INTO pms.patient VALUES(+'"+str(name)+"', '"+str(phoneNumber)+"', '"+str(bloodGroup)+"', '"+str(email)+"', '"+str(password)+"')")


        db.commit()

    def checkLogInInfo(self, email, password):
        pass

