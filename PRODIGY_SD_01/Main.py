
from tkinter import *
from Temperature import *

def clicked():
    temperature = Temperature(int(txt.get()), v.get())
    result = temperature.Result()
    lbl_1.insert(0,str(result["unit 1"]))
    lbl_2.insert(0,str(result["unit 2"]))
    lbl_3.insert(0,str(result["unit 1 result"]))
    lbl_4.insert(0,str(result["unit 2 result"]))

root = Tk()
root.title("Temperature Converter")
#root.geometry('380x200')

lbl = Label(root, text="Enter the Temperature")
lbl.grid(column=0, row=0)

txt = Entry(root, width=20)
txt.grid(column=1, row=0)

v = StringVar(root, "Degree Celsius")  # Default unit selection

k = Radiobutton(root, text="Degree Celsius", variable=v, value="Degree Celsius")
k.grid(column=0, row=1)
k = Radiobutton(root, text="Fahrenheit", variable=v, value="Fahrenheit")
k.grid(column=1, row=1)
k = Radiobutton(root, text="Kelvin", variable=v, value="Kelvin")
k.grid(column=2, row=1)

btn = Button(root, text="Submit", fg="red", command=clicked)
btn.grid(column=1, row=2)

lbl_1 = Entry(root,width=10, fg='blue',font=('Arial',16,'bold'))
lbl_1.insert(0,"")
lbl_1.grid(column=0, row=3)
lbl_2 = Entry(root,width=10, fg='blue',font=('Arial',16,'bold'))
lbl_2.insert(0,"")
lbl_2.grid(column=1, row=3)
lbl_3 = Entry(root,width=10, fg='blue',font=('Arial',16,'bold'))
lbl_3.insert(0,"")
lbl_3.grid(column=0, row=4)
lbl_4 = Entry(root,width=10, fg='blue',font=('Arial',16,'bold'))
lbl_4.insert(0,"")
lbl_4.grid(column=1, row=4)

root.mainloop()
