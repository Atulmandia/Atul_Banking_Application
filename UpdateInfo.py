from backToProfile import backToProfile
from MySQL_Connect import connect

#UpdateInfo function provides an option to update user information like name, mobile number & address.
#This gives option to update all three at the same time.
#If they want to update only one or two of the informatio, they can leave the rest of the information as it is.
def UpdateInfo(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    cursor.execute("select Name, Mobile_number, Address from User where Username=%s",(username,))
    result=cursor.fetchone()
    name=result[0]
    mobNo=result[1]
    address=result[2]
    print(f'\nYour last entered Information is as follows:')
    print(f'Name: {name}')
    print(f'Mobile Number: {mobNo}')
    print(f'Address: {address}')
    EnteredName=input("\nEnter Your Updated Name: ")
    EnteredMobNo=input("Enter New Mobile Number: ")
    EnteredAddress=input("Enter Your New Address: ")
    cursor1=connection.cursor(buffered=True)
    cursor1.execute("update User set Name=%s , Mobile_number=%s,Address=%s where Username=%s",(EnteredName,EnteredMobNo,EnteredAddress,username,))
    print(f'\n \n UPDATED VALUES \n')
    print(f'Now Your Current Name is : {EnteredName}')
    print(f'Now Your Current Mobile Number is : {EnteredMobNo}')
    print(f'Now Your Current Address is : {EnteredAddress}')
    backToProfile(username)