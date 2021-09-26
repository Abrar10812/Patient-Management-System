import sys
sys.path.append('D:\Summer21\CSE470\Project\MVCStructure')
import tkinter as tk
root = tk.Tk()
root.title("Patient Management System")
root.iconbitmap(r'D:\Summer21\CSE470\Project\MVCStructure\View\favicon.ico')

HEIGHT = 500
WIDTH = 800

def bTH():
   root.destroy()
   import View.patientHomePage

#canvas/ container
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg = '#A7B3FD',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx= 0.5, rely=0.5, relwidth= 0.4, relheight= 0.95, anchor= 'center')

#Appointment Successfully Added Label
appointmentSuccessfullyAdded = tk.Label(frame, bg ='green', text="Appointment Successfully Added!", font= 5)
appointmentSuccessfullyAdded.place(relx=0.5, rely=0.2,relheight= 0.2,relwidth= 0.9, anchor='n')

#back to home button
backToHome= tk.Button(frame, text="Back To Home", bg='blue', fg='white', font= 3, command = bTH)
backToHome.place(relx=0.5, rely=0.6, relwidth=0.9, anchor= 'center')

#log out button
logoutbt = tk.Button(frame, text="Log out", bg='red', fg='white', font= 3, command = root.destroy)
logoutbt.place(relx=0.5, rely=0.7, relwidth=0.9, anchor= 'center')

root.mainloop()