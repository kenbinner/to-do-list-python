import sqlite3
import dbcommand

# Print out To-do list for user
def getToDo():
    list = dbcommand.getData()
    return list

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
def addItem(addItem):
    dbcommand.insertData(addItem)

# Removing a to do
def removeItem():
    removeItemId = input('Remove item id... :')
    removedRow = dbcommand.getDataRow(removeItemId)
    dbcommand.removeData(removeItemId)
    print('Removed "' + str(removedRow[0][1]) + '"')
    print('')
    getToDo()

conn = sqlite3.connect("tododatabase.db")

curr = conn.cursor()

#getToDo()
#optionDialog()
