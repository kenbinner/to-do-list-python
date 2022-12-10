import sqlite3
import dbcommand

list = ['Clean my room', 'Buy Groceries']

# Print out To-do list for user
def printToDo():
    print('To do:')
    print('------')
    index = 1
    # >> list = dbcommand.printData()
    for item in list:
        print(str(index) + " | " + item)
        index+=1
    print('------')
    print('')

# Option dialog
def optionDialog():
    print('Choose an Option:')
    print(' Add to do | Type "1"')
    print(' Remove to do | Type "2"')
    print(' Exit | Type "3"')
    option = input('Option : ' )
    if option == "1":
        addItem()
        optionDialog()
    elif option == "2":
        removeItem()
        optionDialog()
    elif option == "3":
        exit()
    else:
        print('Input something else')
        optionDialog()
        
# Adding a new to do
def addItem():
    addItem = input('Add new todo... : ' )
    list.append(addItem)
    print('Added!')
    print('')
    printToDo()

# Removing a to do
def removeItem():
    removeItem = input('Remove item id... :')
    removedItem = list[int(removeItem)-1]
    list.remove(removedItem)
    print('Removed "' + removedItem + "'")
    print('')
    printToDo()

conn = sqlite3.connect("tododatabase.db")

curr = conn.cursor()

printToDo()
optionDialog()
