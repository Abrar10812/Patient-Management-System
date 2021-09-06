import tkinter as tk
root = tk.Tk()
HEIGHT = 500
WIDTH = 800

#canvas/ container
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#frame/ a box
frame = tk.Frame(root, bg = '#F8F8FF',  highlightcolor="black", highlightthickness=2, bd=2)
frame.place(relx= 0.5, rely=0.5, relwidth= 0.4, relheight= 0.95, anchor= 'center')

#Welcome
welcome = tk.Label(frame, text="Welcome", font= 5)
welcome.place(relx=0.5, rely=0.1, anchor='n')

#Add appointment button
addappbt = tk.Button(frame, text="Add appointment", bg='#001EB9', fg='white', font= 3)
addappbt.place(relx=0.5, rely=0.3, relwidth=0.9, anchor= 'center')

#edit info button
editinfobt = tk.Button(frame, text="edit info", bg='#659EC7', fg='white', font= 3)
editinfobt.place(relx=0.5, rely=0.5, relwidth=0.9, anchor= 'center')

#log out button
logoutbt = tk.Button(frame, text="Log out", bg='red', fg='white', font= 3)
logoutbt.place(relx=0.5, rely=0.7, relwidth=0.9, anchor= 'center')

root.mainloop()