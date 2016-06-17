import Tkinter

master = Tkinter.Tk()
l1 = Tkinter.Label(master, text="Label1").grid(row=0)
l2 = Tkinter.Label(master, text="Label2").grid(row=1)

b1 = Tkinter.Button(master, text="Button")

e1 = Tkinter.Entry(master)
e2 = Tkinter.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()
