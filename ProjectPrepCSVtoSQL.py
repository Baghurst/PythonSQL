import sqlite3
with sqlite3.connect("user_email.db") as db:
    
    cursor=db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
Username text NOT NULL,
Login_email text NOT NULL,
Identifier text NOT NULL,
First_Name text NOT NULL,
Last_Name text NOT NULL

) ;""")

# io = open("user_email.csv", "r")
# 
# userAddUsername = input("Add a username: ")
# userAddEmail = input("Add an email: ")
# userAddIdentifier = input("Add an identifier: ")
# userAddFirstName = input("Add a first name: ")
# userAddLastName = input("Add a last name: ")
# 
# io.write("\n")
# io.write(f"5,{userAddUsername}, {userAddEmail}, {userAddIdentifier}, {userAddFirstName}, {userAddLastName}")
# io.write("\n")
# io.close()
io= open("user_email.csv", "r")
header=io.readline()
for line in io:
    line=line.strip()
    line=line.split(",")
    print(line)
    cursor.execute("""INSERT INTO employees(Username,Login_email,Identifier,First_Name,Last_Name)
    VALUES(?,?,?,?,?)""",(list[0],list[1],list[2],list[3],list[4]))
    db.commit()
    print(line)
    
io.close()
