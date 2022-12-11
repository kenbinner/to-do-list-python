import sqlite3
import dbcommand

# Print out To-do list for user
def printToDo():
    print('To do:')
    print('------')
    list = dbcommand.getData()
    for item in list:
        print(str(item[0]) + " | " + str(item[1]))
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
    dbcommand.insertData(addItem)
    print('Added!')
    print('')
    printToDo()

# Removing a to do
def removeItem():
    removeItemId = input('Remove item id... :')
    removedRow = dbcommand.getDataRow(removeItemId)
    dbcommand.removeData(removeItemId)
    print('Removed "' + str(removedRow) + "'")
    print('')
    printToDo()

conn = sqlite3.connect("tododatabase.db")

curr = conn.cursor()

printToDo()
optionDialog()
