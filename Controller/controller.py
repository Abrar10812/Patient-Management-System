import sys

import Model.doctorDb

sys.path.append('D:\Summer21\CSE470\Project\MVCStructure')

def signUpClicked():
    import View.signUppage
    #execfile('signUppage.py')


def signUpbuttonClicked(entryName, entryPhone, bloodGroup, entryEmail, entryPass):
    name = str(entryName)
    phone = str(entryPhone)
    email = str(entryEmail)
    password = str(entryPass)

    import Model.patientDb
    pDb = Model.patientDb.patientDb()
    pDb.newUserSignUp(name, phone, bloodGroup, email, password)

def logIn(email, password):
    import Model.patientDb
    testIfEqual= Model.patientDb.checkLogInInfo(email, password)

def fetchDoctorlist():
    docListFromModel = Model.doctorDb.doctorList()
    return docListFromModel

def doctorInfowithQual():
    import Model.doctorDb
    x = Model.doctorDb.showDoctorInfo()
    return x





