import sqlite3

db = sqlite3.connect("Mellia.db")
mycursor = db.cursor()

Mellia_user = '''
    CREATE TABLE Mellia_user
    (
        id INT PRIMARY KEY,
        username VARCHAR(60),
        password VARCHAR(60),
        phonenb VARCHAR(20),
        role VARCHAR(60),
        email VARCHAR(60),
        firstname VARCHAR(60),
        lastname VARCHAR(60),
        avt VARCHAR(500)
    );
'''

Setbill = '''
    CREATE TABLE Mellia_bill
    (
        tb VARCHAR(60) PRIMARY KEY,
        total INT,
        settime DATETIME,
        method VARCHAR(30),
        coupon INT
    );
'''
Mellia_order = '''
    CREATE TABLE Mellia_orders(
        id INT PRIMARY KEY,
        tb VARCHAR(10),
        quantity INT,
        order_slot INT,
        product VARCHAR(100),
        price FLOAT,
        staffname VARCHAR(60),
        status VARCHAR(60)
    );
'''
Order = '''
    CREATE TABLE orders(
        id INT PRIMARY KEY,
        quantity INT,
        order_slot INT,
        product VARCHAR(100),
        price INT
    )
'''
productsb = '''
    CREATE TABLE productsb(
        id INT PRIMARY KEY,
        name VARCHAR(500),
        price FLOAT,
        content VARCHAR(500),
        image VARCHAR(500)
    )
'''
producttb = '''
    CREATE TABLE producttb(
        id INT PRIMARY KEY,
        name VARCHAR(500),
        price FLOAT,
        content VARCHAR(500),
        image VARCHAR(500)
    )
'''
Value = [
    {
        "id":1,
        "username":"minhquoc",
        "password":"minhquoc",
        "phonenb":"0766709535",
        "role":"Admin",
        "email":"mtranquoc77@gmail.com",
        "firstname":"Tran Quoc",
        "lastname":"Minh",
        "avt":"C:/Mellia/User/BABY.png",

    },
]

Username = '''
    INSERT INTO Mellia_user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
'''


DropCol = '''ALTER TABLE orders DROP COLUMN price'''
NewCol = '''ALTER TABLE orders ADD COLUMN price FLOAT'''
Table = '''PRAGMA table_list'''

Drop = '''DROP TABLE productsb'''

try:
    if sqlite3.Connection:
        print("DB connected")
        for obj in Value:
            mycursor.execute(Username,
                (
                    obj["id"],
                    obj["username"],
                    obj["password"],
                    obj["phonenb"],
                    obj["role"],
                    obj["email"],
                    obj["firstname"],
                    obj["lastname"],
                    obj["avt"]
                )
            )
        
        
        # mycursor.execute()
        # # for obj in mycursor.fetchall():
        # #     print(obj)
        # # mycursor.execute(producttb)
        print("Command Confirm")

        db.commit()
    else :
        print("Not connected")

except sqlite3.Error as error:
    print(error)