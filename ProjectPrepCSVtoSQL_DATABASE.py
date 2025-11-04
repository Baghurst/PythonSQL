import sqlite3
with sqlite3.connect("user_email.db") as db:    
    cursor=db.cursor()
    
while True:
    userAddUsername = input("Add a username: ")
    if userAddUsername == condition:
        ready to add to database
        break
    else:
        print("invalid input")
        continue  
userAddUsername = input("Add a username: ")
userAddEmail = input("Add an email: ")
userAddIdentifier = input("Add an identifier: ")
userAddFirstName = input("Add a first name: ")
userAddLastName = input("Add a last name:")


cursor.execute("""INSERT INTO employees(Username,Login_email,Identifier,First_Name,Last_Name)
    VALUES(?,?,?,?,?)""",(userAddUsername[0],userAddEmail[1],userAddIdentifier[2],userAddFirstName[3],userAddLastName[4]))
db.commit()
    
#cursor.execute("SELECT * FROM employees")
#print(cursor.fetchall())
    