import sqlite3
connection_obj = sqlite3.connect("testphase.db")

mycursor = connection_obj.cursor()
ScriptDB = '''
    SELECT * FROM User
'''
Creation = '''
    CREATE TABLE User 
    (id INT PRIMARY KEY, name VARCHAR(50), age INT)    
'''

Record = [
    {
        "id":2,
        "name":"toan",
        "age":20
    },
    {
        "id":3,
        "name":"dung",
        "age":20
    },
    {
        "id":4,
        "name":"khanh",
        "age":20
    },
]
RecordIndex = '''
    INSERT INTO User VALUES (?,?,?)
'''

try:
    if sqlite3.Connection:
        print("connection DB is Reaveal")
        # for obj in Record:
        #     mycursor.execute(RecordIndex,(obj['id'],obj['name'],obj['age']))
        mycursor.execute(ScriptDB)
        for obj in mycursor.fetchall():
            print(obj[0]," - ",obj[1]," - ",obj[2])
        connection_obj.commit()
    else:
        print("Connection interrupted")
except sqlite3.Error as error:
    print(error)