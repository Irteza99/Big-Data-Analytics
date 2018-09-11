import sqlite3

def createTable():
    connection = sqlite3.connect("login.db")

    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PHONE INTEGER,PASSWORD TEXT NOT NULL,CATEGORY TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",('irteza','irtezacool99ali@gmail.com','9889622731','alibaba40chor','Intern'))

    connection.commit()
                       
    result = connection.execute("SELECT * FROM USERS")
                       
    for data in result:
        print("Username : ",data[0])
        print("Email : ",data[1])
        print("Phone : ",data[2]) 
        print("Password : ",data[3])
        print("Category : ",data[4])
    connection.close()
createTable()
         
