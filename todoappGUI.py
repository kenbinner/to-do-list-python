from tkinter import *
from PIL import Image, ImageTk
import todoapp

window = Tk()
window.title("To do list")

lbl_title = Label(master = window, text="To do List", height=5, padx=20)
lbl_title.grid(row = 0, column=0)

# image import + resizing
check_image = Image.open("./assets/check.png")
check_image_resized = check_image.resize((20,20))
check_icon = ImageTk.PhotoImage(check_image_resized)

#displaying to do list
listx = 1

def displayList():
    global listx

    list=todoapp.getToDo()

    listx = 1

    for item in list:
        lbl_item = Label(master=window, text=str(item[0]) + " | " + str(item[1]), height=5, padx=20)
        lbl_item.grid(row=listx, column=0, sticky=W)

        btn_tick = Button(master=window, image=check_icon)
        btn_tick.grid(row=listx, column=2)
        listx+=1

    
    if refreshedList:
        btn_add.grid_forget()
    btn_add.grid(row= listx, column=1)


#showing_add_options toggle condition
showing_add_options = False

# Add to do functionality
def addButtonClicked():
    global showing_add_options

    if showing_add_options:
        hideAddOptions()
    else:
        showAddOptions()
        
def showAddOptions():
    global showing_add_options

    ent_addToDo.grid(row=listx+1, column=0)
    btn_submit.grid(row=listx+1, column=2)
    showing_add_options = True

def hideAddOptions():
    global showing_add_options
    
    ent_addToDo.grid_forget()
    btn_submit.grid_forget()
    showing_add_options = False

# Refreshed list condition
refreshedList = False

def submitButtonClicked():
    global refreshedList

    todoapp.addItem(str(newToDo_var.get()))
    refreshedList = True
    hideAddOptions()
    displayList()

btn_add = Button(master=window, text="Add to do", relief=RAISED, borderwidth=1, command=addButtonClicked)

displayList()

newToDo_var = StringVar()
ent_addToDo = Entry(master=window, textvariable=newToDo_var)

btn_submit = Button(master=window, text="Add", relief=RAISED, command=submitButtonClicked)

window.mainloop()