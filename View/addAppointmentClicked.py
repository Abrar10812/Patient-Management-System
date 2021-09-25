import sys
sys.path.append('D:\Summer21\CSE470\Project\MVCStructure')
import tkinter as tk
root = tk.Tk()
root.title("Patient Management System")
root.iconbitmap(r'D:\Summer21\CSE470\Project\MVCStructure\View\favicon.ico')
import Controller.controller

HEIGHT = 500
WIDTH = 800

def back():
    root.destroy()
    import View.patientHomePage

def docOptionList():
    docop = Controller.controller.fetchDoctorlist()
    return docop

#canvas/ container
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg = '#A7B3FD',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx= 0.5, rely=0.5, relwidth= 0.4, relheight= 0.95, anchor= 'center')

#Add Appointment label
addAppointment = tk.Label(frame, bg ='#D7B9DF', text="Add Appointment", font= 5)
addAppointment.place(relx=0.5, rely=0.1, anchor='n')

#Add appointment button
doctorInfo = tk.Button(frame, text="Doctor Info", bg='green', fg='white', font= 3)
doctorInfo.place(relx=0.5, rely=0.3, relwidth=0.9, anchor= 'center')

#Doctor option menu

option_list = docOptionList()
value_inside = tk.StringVar(frame)
value_inside.set("Select Doctor")
doc = tk.OptionMenu(frame, value_inside, *option_list)
doc.place(relx=0.5, rely=0.4, relwidth = 0.9, anchor ='n')
Doctor = value_inside.get()

#Select time Label
selectTimeLabel = tk.Label(frame, bg ='#D7B9DF', text="Select Time in Detail", font= 3)
selectTimeLabel.place(relx=0.3, rely=0.5, anchor='n')

#entrySelectTime
selectTime = tk.Entry(frame)
selectTime.place(relx=0.5, rely=0.55, relheight=0.05, relwidth=0.9, anchor='n')

#Add appointment button
addappbt = tk.Button(frame, text="Add appointment", bg='#001EB9', fg='white', font= 3)
addappbt.place(relx=0.5, rely=0.8, relwidth=0.9, anchor= 'center')

#back button
backbt = tk.Button(frame, text="back", bg='red', fg='white', font= 3, command =back)
backbt.place(relx=0.5, rely=0.9, relwidth=0.9, anchor= 'center')

root.mainloop()