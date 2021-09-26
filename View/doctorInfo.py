import sys
sys.path.append('D:\Summer21\CSE470\Project\MVCStructure')
import tkinter as tk
root = tk.Tk()
root.title("Patient Management System")
root.iconbitmap(r'D:\Summer21\CSE470\Project\MVCStructure\View\favicon.ico')

HEIGHT = 500
WIDTH = 800

def back():
    root.destroy()
    import View.patientHomePage

def fetchDoctorInfo():
    import Controller.controller
    doctorlist= Controller.controller.doctorInfowithQual()
    print (doctorlist)
    return doctorlist

#canvas/ container
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg = '#A7B3FD',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx= 0.5, rely=0.5, relwidth= 0.7, relheight= 0.95, anchor= 'center')

#DoctorInfoLabel
doctorInfoLabel = tk.Label(frame, bg ='#D7B9DF', text="Doctor Info", font= 5)
doctorInfoLabel.place(relx=0.5, rely=0.1, anchor='n')

#DoctorNameQualSpecialityLabel
doctorNQSLabel = tk.Label(frame, bg ='#D7B9DF', text="Name                      Qualification               Speciality", font= 5)
doctorNQSLabel.place(relx=0.5, rely=0.2, anchor='n')

#DoctorInfoListLabel
doctorInfoListLabel = tk.Label(frame, bg ='yellow', text=fetchDoctorInfo(), font= 1)
doctorInfoListLabel.place(relx=0.5, rely=0.3, relheight= 0.5, anchor='n')

#back button
backbt = tk.Button(frame, text="back", bg='red', fg='white', font= 3, command =back)
backbt.place(relx=0.5, rely=0.9, relwidth=0.9, anchor= 'center')

root.mainloop()