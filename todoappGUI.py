from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("To do list")
window.geometry('300x400')
#window.configure(background = "white")

lbl_title = Label(master = window, text="To do List", height=5, padx=20)
lbl_title.grid(row = 0, column=0)

list=("todo1","todo2","todo3")
listx = 1
check_image = Image.open("./assets/check.png")
check_image_resized = check_image.resize((20,20))
check_icon = ImageTk.PhotoImage(check_image_resized)
for item in list:
    lbl_item = Label(master=window, text=item, height=5, padx=40)
    lbl_item.grid(row=listx, column=0)

    btn_tick = Button(master=window, image=check_icon)
    btn_tick.grid(row=listx, column=2)
    listx+=1

btn_add = Button(master=window, text="Add to do", relief=RAISED, borderwidth=1)
btn_add.grid(row= listx, column=1)

window.mainloop()

"""
top = Label(window , text = "My To Do list", padx=50, pady = 40).grid(row=0, column=0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()
"""

"""window = tk.Tk()

frame_a = tk.Frame(width=150, height=200)
frame_a.pack()

title = tk.Label(master = frame_a, text="My To do list")
title.place(x=10, y=20)

button = tk.Button(master=frame_a, text="Add to do", width = 10, height = 3)
button.place(x = 10, y = 40)

newTodoEntry = tk.Entry(master=frame_a, width = 100)
newTodoEntry.place(x = 10, y = 90)

if newTodoEntry.get() == "trigger":
    newTodoEntry.delete(0,tk.END)

window.mainloop()
"""