from pprint import  pprint
from backToProfile import backToProfile
from execution import cur
from MySQL_Connect import connect

#AddBeneficiary function helps us to create an option for user to add a beneficiary to his/her account.
def AddBeneficiary(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    name=input('\n Enter Beneficiary name: ')
    accountNo=input('\n Enter Beneficiary account number: ')
    ifsc=input('\n Enter Beneficiary IFSC Code: ')
    cursor1=connection.cursor(buffered=True)
    cursor1.execute("select * from Beneficiary")
    Ben_id=cursor1.rowcount+1
    cursor.execute("insert into Beneficiary values(%s,%s,%s,%s,%s)",(Ben_id,name,accountNo,ifsc,username))
    backToProfile(username)
#viewBeneficiary function helps us to show list of beneficiary accounts added to a particular account.
def viewBeneficiary(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    cursor.execute("select Name,Account_number,IFSC from Beneficiary where Username=%s ",(username,))
    result=cursor.fetchall()
    names=[row[0] for row in result]
    accountNos=[row[1] for row in result]
    ifscs=[row[2] for row in result]
    i=1
    for(name,accountNo,ifsc) in zip(names,accountNos,ifscs):
        pprint(i)
        pprint("Beneficiary Account details are as below: ")
        pprint(f'Name is {name}')
        pprint(f'Account Number is {accountNo}')
        pprint(f'IFSC code is {ifsc}')
        i+=1
    backToProfile(username)