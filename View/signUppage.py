import tkinter as tk
root = tk.Tk()
HEIGHT = 500
WIDTH = 600

#canvas/ container
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg = '#F8F8FF',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx= 0.5, rely=0.5, relwidth= 0.4, relheight= 0.95, anchor= 'center')

#label
label = tk.Label(frame, text="Patient Management System", font= 0.1)
label.place(relx=0.5, rely=0.04, anchor ='n')

#label
label = tk.Label(frame, text="Create a new account", font= 0.1)
label.place(relx=0.5, rely=0.1, anchor ='n')

#nameLabel
nameLabel = tk.Label(frame, text="Name")
nameLabel.place(relx=0.17, rely=0.2, anchor='ne')

#entryName/input Name
entryName= tk.Entry(frame)
entryName.place(relx= 0.45, rely=0.25, relheight=0.05, relwidth=0.9, anchor='n')

#phoneLabel
phoneLabel = tk.Label(frame, text="Phone")
phoneLabel.place(relx=0.17, rely=0.3, anchor='ne')

#entryPhone/input Phone
entryPhone= tk.Entry(frame)
entryPhone.place(relx= 0.45, rely=0.35, relheight=0.05, relwidth=0.9, anchor='n')

#BGLabel
BGLabel = tk.Label(frame, text="Blood Group")
BGLabel.place(relx=0.3, rely=0.4, anchor='ne')

#BG option menu
option_list = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
value_inside = tk.StringVar(frame)
value_inside.set("Select an Option")
selectCat = tk.OptionMenu(frame, value_inside, *option_list)
selectCat.place(relx=0.28, rely=0.45, anchor ='n')

#emailLabel
emailLabel = tk.Label(frame, text="Email")
emailLabel.place(relx=0.15, rely=0.53, anchor='ne')

#entryEmail/input email
entryEmail= tk.Entry(frame)
entryEmail.place(relx= 0.45, rely=0.58, relheight=0.05, relwidth=0.9, anchor='n')

#passLabel
passLabel = tk.Label(frame, text="Password")
passLabel.place(relx= 0.23, rely=0.63, anchor='ne')

#entryPass/input password
entryPass= tk.Entry(frame)
entryPass.place(relx= 0.45, rely=0.68,relheight=0.05, relwidth=0.9, anchor='n')

#confirmPassLabel
confirmPassLabel = tk.Label(frame, text="Confirm Password")
confirmPassLabel.place(relx= 0.43, rely=0.73, anchor='ne')

#entryPass/input password
entryconPass= tk.Entry(frame)
entryconPass.place(relx= 0.45, rely=0.78, relheight=0.05, relwidth=0.9, anchor='n')

#sign up button
signupbt = tk.Button(frame, text='Sign up', bg='#00FF00', font= 3)
signupbt.place(relx= 0.45, rely= 0.95, relwidth= 0.5, anchor= 'center')

root.mainloop()