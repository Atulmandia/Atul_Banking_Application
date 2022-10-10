from MySQL_Connect import connect
from backToProfile import backToProfile

#defining IFSC code for our banking application.
#this will help us recognize if the recipient account holder is of our bank or not.
IFSC="ATUL000011"

#Transaction function helps to do all the necessary addition, subtraction & entries of transactions.
def Transaction(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    print(f'\nFill the following details: ')
    toAccount=input("Enter Recipient Account Number: ")
    amount=int(input("Enter Amount to transfer: "))
    ifsc=input("Enter Recipient IFSC code: ")
    name=input("Enter Recipient name : ")
    print(f'\nPAYMENT GATEWAY')
    print(f"{amount} needs to be send to {name} Account Number:{toAccount}")
    print(f'Select your Card Type \n 1. Credit Card \n 2. Debit Card')
    selectedOption=int(input("Select either 1 or 2: "))
    CardTyped=CardType(selectedOption)

    CardNumber=int(input("\nEnter Your Card Number: "))
    print(CardNumber)
    cvv=int(input("Enter Card CVV: "))
    pin=int(input("Enter Your PIN: "))
    cursor1=connection.cursor(buffered=True)
    cursor1.execute("Select * from Cards where Card_number=%s and Card_type=%s and Pin=%s and CVV=%s",(CardNumber,CardTyped,pin,cvv,))
    print(cursor1.fetchone())
    if(cursor1.rowcount < 0):
        print("Entered Card is Wrong!!")
        Transaction(username)
    else:
        cursor3=connection.cursor(buffered=True)
        cursor3.execute("select * from Account where Username=%s",(username,))
        result=cursor3.fetchone()
        fromAccount=result[0]
        fromAccountBalance=result[2]
        cursor8=connection.cursor(buffered=True)
        cursor8.execute("select * from Transactions")
        noTransaction= cursor8.rowcount
        if ifsc==IFSC:
            cursor2= connection.cursor(buffered=True)
            cursor2.execute("select * from Account where Account_number=%s",(toAccount,))
            result1=cursor2.fetchone()
            print(result1)
            # curdate='curdate()'
            if cursor2.rowcount<0 :
                print(f'Recipient Account does not exist')
            else:
                # result1=cursor2.fetchone()
                toAccountBalance=result1[2]
                cursor4=connection.cursor(buffered=True)
                cursor4.execute("update Account set Account_balance=%s where Account_number=%s",(fromAccountBalance-amount,fromAccount,))
                cursor5=connection.cursor(buffered=True)
                cursor5.execute("update Account set Account_balance=%s where Account_number=%s",(toAccountBalance+amount,toAccount,))
                cursor7=connection.cursor(buffered=True)
                cursor7.execute("insert into Transactions (TransactionID, Amount_value, From_Account, To_Account, Balance_left, Card_number, Date, IFSC, Recipient_name) values(%s,%s,%s,%s,%s,%s,curdate(),%s,%s)",(noTransaction+1,-1*amount,fromAccount,toAccount,fromAccountBalance-amount,CardNumber,ifsc,name,))
                cursor9=connection.cursor(buffered=True)
                cursor9.execute("insert into Transactions (TransactionID, Amount_value, From_Account, To_Account, Balance_left, Card_number, Date, IFSC, Recipient_name) values(%s,%s,%s,%s,%s,%s,curdate(),%s,%s)",(noTransaction+2,amount,fromAccount,toAccount,toAccountBalance+amount,CardNumber,ifsc,name,))
        else:
            cursor6=connection.cursor(buffered=True)
            cursor6.execute("update Account set Account_balance=%s where Account_number=%s",(fromAccountBalance-amount,fromAccount,))
            cursor10=connection.cursor(buffered=True)
            cursor10.execute("insert into Transactions (TransactionID, Amount_value, From_Account, To_Account, Balance_left, Card_number, Date, IFSC, Recipient_name) values(%s,%s,%s,%s,%s,%s,curdate(),%s,%s)",(noTransaction+1,-1*amount,fromAccount,toAccount,fromAccountBalance-amount,CardNumber,ifsc,name,))
    backToProfile(username)

#CardType function will take evaluate and switch transaction through credit & debit card and at the same time checks the entered card number whether it is wrong or right.
def CardType(selectedOption):
    if selectedOption==1:
         return "Credit_card"
    elif selectedOption==2:
        return "Debit_card"
    else: 
        selectedOption=int(input("Entered Card Type again"))
        print(selectedOption)
        return CardType(selectedOption)