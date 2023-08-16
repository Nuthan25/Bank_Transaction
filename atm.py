def deposit():
    depo=int(input("Enter the amount to Deposit : "))
    print(depo ," Amount added successfully")
    tamount=tamount+depo
    balance()

def balance():
   
    print("please choose \n1.Deposit Amount \n2.Withdraw Amount \n3.Balance")
    a=int(input("Enter the value \n"))

    if(a==1):
        deposit()
    elif(a==2):
        withdraw()
    elif(a==3):
        print("Balance is :")


    
def withdraw():
    wit=int(input("Enter the amount to Withdraw : "))
    withd=wit
    print(withd) 
    balance()   

balance()



import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",database="databaseName" )
cursor = connection.cursor()
connection.close()

import pymysql
connection=pymysql.connect(host="localhost", user="root", passwd="", 
database="databaseName")
cursor = connection.cursor()
runtable= """CREATE TABLE order(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME CHAR(20) NOT NULL,
TRACK CHAR(10))"""
cursor.execute(runtable )
connection.close()


import pymysql
connection = pymysql.connect(host="localhost", user="root", passwd="", 
database="databaseName")
cursor = connection.cursor()
insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES('Sharath', 'M' );"
cursor.execute(insert1)
connection.commit()
connection.close()


import pymysql
connection = pymysql.connect(host="localhost", user="root", passwd="", 
database="databaseName")
cursor = connection.cursor()
retrive = "Select * from Artists;"
cursor.execute(retrieve)
rows = cursor.fetchall()
for row in rows:
 print(row)
connection.commit()
connection.close()