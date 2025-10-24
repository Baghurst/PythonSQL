import sqlite3
with sqlite3.connect("company.db") as db:
    cursor=db.cursor()
'''cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
    id integer PRIMARY KEY,
    name text NOT NULL,
    dept text NOT NULL,
    salary integer) ;""")

newID = input("Enter ID number: ")
newName = input("Enter name: ")
newDept = input("Enter department: ")
newSalary = input("Enter salary: ")
cursor.execute("""INSERT INTO employees(id,name,dept,salary)
    VALUES(?,?,?,?)""",(newID,newName,newDept,newSalary))
db.commit()
'''
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

#cursor.execute("SELECT * FROM employees")
#for x in cursor.fetchall():
 #   print(x)
    
    cursor.execute("SELECT * FROM employees ORDER BY name")
for x in cursor.fetchall():
    print(x)
    
    Test =   cursor.execute("SELECT * FROM employees WHERE salary>20000")
    Test2 =  cursor.execute("SELECT * FROM employees WHERE dept='Sales'")
    Test3 =  cursor.execute("SELECT id,name,salary FROM employees")
    
    whichDept = input("Enter a department: ")
    cursor.execute("SELECT * FROM employees WHERE dept=?", [whichDept])
    for x in cursor.fetchall():
        print(x)
        
        cursor.execute("UPDATE employees SET name ='Tony' WHERE id=1")
        db.commit()
        
        cursor.execute("DELETE employees WHERE id=1")
        
    
    

db.close()




    
    
