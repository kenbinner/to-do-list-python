import sqlite3

def createTable():
    createTableCommand = """ CREATE TABLE TODO_LIST (
    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
    item VARCHAR(100)
    );"""

    curr.execute(createTableCommand)
    conn.commit()

def dropTable():
    dropTableCommand = """ DROP TABLE TODO_LIST"""

    curr.execute(dropTableCommand)
    conn.commit()
    print('dropped table')

def otherCommand():
    #otherCommand = """ SET IDENTITY_INSERT TODO_LIST OFF"""
    #otherCommand = """ALTER TABLE TODO_LIST auto_increment = 1;"""
    otherCommand = """SELECT * FROM sqlite_sequence;"""

    #curr.execute(otherCommand)
    #conn.commit()

    curr.execute(otherCommand)
    print(curr.fetchall)

def createIndex():
    createIndexCommand = """ CREATE UNIQUE INDEX indItem
    on TODO_LIST (item) """

    curr.execute(createIndexCommand)
    conn.commit()

def insertData(item):
    #addData = "INSERT INTO TODO_LIST VALUES('" + str(index) + "', '" + item + "');"
    addData = "insert into TODO_LIST(item) values('" + item + "');"

    curr.execute(addData)
    conn.commit()

def removeData(itemId):
    removeDataCommand = """DELETE FROM TODO_LIST 
    WHERE itemId = '""" + str(itemId) + "';"

    curr.execute(removeDataCommand)
    conn.commit()

    shiftIds = """UPDATE TODO_LIST SET itemId = itemId - 1 WHERE itemId > '""" + str(itemId) + "';"

    curr.execute(shiftIds)
    conn.commit()

    resetSequence = """delete from sqlite_sequence where name='TODO_LIST';"""

    curr.execute(resetSequence)
    conn.commit()


def getData():  
    fetchData = "SELECT * from TODO_LIST"
    
    curr.execute(fetchData)
    return curr.fetchall()

def getDataRow(itemId):
    fetchData = """SELECT * from TODO_LIST
    WHERE itemId = '""" + str(itemId) + "';"

    curr.execute(fetchData)
    return curr.fetchall()

def printDataTest():  
    fetchData = "SELECT * from TODO_LIST"
    
    data = curr.execute(fetchData)
    for i in data:
        print(i)

conn = sqlite3.connect("tododatabase.db")

curr = conn.cursor()

#createTable()
#dropTable()

#createIndex()
#insertData(0, 'Play Games')
#insertData('Eat cheese')
#removeData(10)
#printDataTest()
#otherCommand()

