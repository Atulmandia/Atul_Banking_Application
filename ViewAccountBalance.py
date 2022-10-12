from pprint import  pprint
from MySQL_Connect import connect
from backToProfile import backToProfile

#viewAccountBalance function helps us to provide an option to display the account balance of the user.
def viewAccountBalance(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    cursor.execute("select * from Account where Username=%s",(username,))
    result1=cursor.fetchall()
    accNumbers=[row[0] for row in result1]
    userName=[row[1] for row in result1]
    balance=[row[2] for row in result1]
    i=1
    for(Account_number, Username, Account_balance) in zip(accNumbers,userName,balance):
        print(i)
        print(f'Your Account number is {Account_number}')
        print(f'Card Type is {Username}')
        print(f'MPIN is {Account_balance}\n')
        i+=1
    backToProfile(username)