list = ['Clean my room', 'Buy Groceries']

# Print out To-do list for user
def printToDo():
    print('To do:')
    print('------')
    for item in list:
        print(item)
    print('------')

# Option dialog
def optionDialog():
    option = input('Add: press 1, Remove: press 2, Exit: 3 : ' )
    if option == "1":
        addItem()
    elif option == "3":
        exit
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
    list.remove(list[removeItem])
    print('Removed!')
    print('')
    printToDo()

printToDo()
optionDialog()
