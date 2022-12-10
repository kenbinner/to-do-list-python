import sqlite3

def createTable():
    createTableCommand = """ CREATE TABLE TODO_LIST (
    indexNum INTEGER,
    item VARCHAR(100)
    );"""

    curr.execute(createTableCommand)
    conn.commit()

def dropTable():
    dropTableCommand = """ DROP TABLE TODO_LIST"""

    curr.execute(dropTableCommand)
    conn.commit()
    print('dropped table')

def insertData(index, item):
    addData = "INSERT INTO TODO_LIST VALUES('" + str(index) + "', '" + item + "');"
    
    curr.execute(addData)
    conn.commit()
    print("The data has been added!")

def removeData(index):
    removeDataCommand = """DELETE FROM TODO_LIST 
    WHERE indexNum = '""" + str(index) + "';"

    curr.execute(removeDataCommand)
    conn.commit()


def printData():  
    fetchData = "SELECT * from TODO_LIST"
    
    curr.execute(fetchData)
    return curr.fetchall()

conn = sqlite3.connect("tododatabase.db")

curr = conn.cursor()

#createTable()
#dropTable()

#insertData(57, 'Play Games')
#insertData(58, 'Eat cheese')
#removeData(57)
printData()
