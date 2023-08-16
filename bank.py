import pymysql

connection=pymysql.connect(host='localhost',user='root',passwd="",database='bank_acc')

cursor=connection.cursor()


def bank():
    a=int(input("Enter your choice: \n1.HOME \n2.REGISTRE FOR ATM SERVICES \n3.ATM \n"))
    if(a==2):
        reg()
    if(a==3):
        atm()

def reg():
    print("=====REGISTER FOR ATM SERVICE====")
    print("========enter your details========")
    name=input("Enter your name: ")
    pnum=int(input("Enter your Mobile Number: "))
    cash=500

    cont="select * from bank where contact='%d'"%pnum
    cursor.execute(cont)
    res=cursor.fetchall()
    if(res):
        print("sorry you already have an account")
    else:
        print("complete the registration process")
        cno=int(input("Enter your DEBIT CARD NO : "))
        atp=int(input("Choose your ATM pin: "))
        regs="insert into bank(name,contact,card_no,atm_pin,balance) values('%s','%d','%d','%d','%d')" %(name,pnum,cno,atp,cash)
        cursor.execute(regs)
        connection.commit()
    bank()

def atm():
    print("=========WELCOME TO ATM SERVICE=========")
    cno = input("Enter your DEBIT CARD NO: ")
    atp = int(input("Enter your ATM pin: "))

    
    select_query = "SELECT * FROM bank WHERE card_no = '%s' AND atm_pin = '%d'" % (cno, atp)
    cursor.execute(select_query)
    result = cursor.fetchone() 

    if result:
        print("Authentication successful!")
        if len(result) >= 5:
            cash = result[5]  
            while True:
                
                print("1. Check balance")
                print("2. Cash withdrawal")
                print("3. Deposit")
                print("4. Quit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("Your current balance is: $", cash)

                elif choice == "2":
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount <= cash:
                        cash -= amount
                        print("Withdrawal successful. Remaining balance: $", cash)
                        cash1="update bank set balance='%d' WHERE card_no = '%s' AND atm_pin = '%d'" %(cash,cno,atp)
                        cursor.execute(cash1)
                        connection.commit()

                    else:
                        print("Insufficient funds. Unable to withdraw.")

                elif choice == "3":
                    amount = int(input("Enter the amount to deposit: "))
                    cash += amount
                    print("Deposit successful. Current balance: $", cash)
                    cash1="update bank set balance='%d' WHERE card_no = '%s' AND atm_pin = '%d'" %(cash,cno,atp)
                    cursor.execute(cash1)
                    connection.commit()

                elif choice == "4":
                    print("Exiting ATM service. Thank you!")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid database record. Unable to retrieve balance.")
    else:
        print("Invalid debit card number or ATM pin. Access denied.")



bank()