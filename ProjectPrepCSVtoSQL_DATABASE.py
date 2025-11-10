import sqlite3
with sqlite3.connect("user_email.db") as db:    
    cursor=db.cursor()
    
condition =0

cursor.execute("SELECT Username FROM employees")
thelist=(cursor.fetchall())
print(thelist)

while condition!=1:
    
    userAddUsername = input("Add a username: ")
    for i in range(len(thelist)):
        if userAddUsername == thelist[i][0]:
            print("That username is already taken!")
            break
        else:
            condition +=1
            print('Your username is added')
            
        


    
'''while True:

    
    userAddEmail = input("Add a username: ")
    if userAddEmail != condition:
        #ready to add to database
        break
    
while True:

    userAddIdentifier = input("Add a username: ")
    if userAddIdentifier != condition:
        #ready
        break

while True:
    
    userAddFirstName = input("Add a username: ")
    if userAddFirstName != condition:
        #ready to add to database
        break
    
while True:

    userAddLastName = input("Add a username: ")
    if userAddLastName != condition:
        #ready to add to database
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
