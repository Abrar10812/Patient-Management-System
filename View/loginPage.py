import sys
sys.path.append('D:\Summer21\CSE470\Project\MVCStructure')
import Controller.controller
import tkinter as tk
root = tk.Tk()

root.title("Patient Management System")
root.iconbitmap(r'D:\Summer21\CSE470\Project\MVCStructure\View\favicon.ico')

HEIGHT = 500
WIDTH = 800

def clickSignUp():
    root.destroy()
    Controller.controller.signUpClicked()

def clickLogIn():
    root.destroy()
    Controller.controller.logIn(entryEmail.get(), entryPass.get())


#canvas/ container
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg='#F8F8FF',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.95, anchor='center')

#label
label = tk.Label(frame, text="Patient Management System", font=0.1)
label.place(relx=0.5, rely=0.1, anchor ='n')

#emailLabel
emailLabel = tk.Label(frame, text="E-mail")
emailLabel.place(relx=0.17, rely=0.4, anchor='ne')

#passLabel
passLabel = tk.Label(frame, text="Password")
passLabel.place(relx=0.125, rely=0.55, anchor='n')

#select category option menu
option_list = ["Patient", "Doctor"]
value_inside = tk.StringVar(root)
value_inside.set("Select an Option")
selectCat = tk.OptionMenu(root, value_inside, *option_list)
selectCat.place(relx=0.5, rely=0.23, anchor='n')

#entryEmail/input email
entryEmail= tk.Entry(frame)
entryEmail.place(relx=0.5, rely=0.45, relheight=0.07, relwidth=0.9, anchor='n')
entryEmail = tk.StringVar()

#entryPass/input password
entryPass= tk.Entry(frame)
entryPass.place(relx=0.5, rely=0.6, relheight=0.07, relwidth=0.9, anchor='n')
entryPass = tk.StringVar()

#login button
loginbt = tk.Button(frame, text="Log in", bg='#659EC7', fg='white', font=3, command=clickLogIn)
loginbt.place(relx=0.5, rely=0.75, relwidth=0.9, anchor='center')

#sign up button
signupbt = tk.Button(frame, text='Sign up', bg='#00FF00', font=3, command=clickSignUp)
signupbt.place(relx=0.5, rely=0.85, relwidth=0.9, anchor='center')
root.mainloop()