list = ['Clean my room', 'Buy Groceries']

def printToDo():
    print('To do:')
    print('------')
    for item in list:
        print(item)

option = input('Add: press 1, Remove: press 2' )

if option == "1":
    addItem = input('Add new todo... :' )
    list.append(addItem)
    print('Added!')
    printToDo()
else:
    exit

# elif option == "2":
#     removeItem = input('Remove item id... :')
#     list.remove(list[removeItem])


