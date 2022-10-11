from pprint import  pprint
from MySQL_Connect import select
from execution import cur

# register function starts asking perrsonal info of the user
def register():
    select()
    username= usernameCheck()
    #pprint(username)
    name = input('\nEnter Your name: ') 
    address = input('\nEnter Your address: ')
    aadhar = aadharCheck() 
    mobile = mobileCheck()
    password = input('\nEnter password: ')
    query = "insert into User values (%s, %s, %s, %s, %s, %s)"
    mycon= cur()
    user_query = (username,name,aadhar,mobile,password,address)
    mycon.execute(query,user_query)

# mobileCheck function takes the mobile number & checks the input if it is 10 digit or not
def mobileCheck():
    mobile_info = input('\nEnter your mobile number: ')
    if len(str(mobile_info))!=10:
        mobile_info = mobileCheck()
    return mobile_info

# aadharCheck function takes the aadhar number & checks the input if it is 12 digit or not
def aadharCheck():
    aadhar_info = input('\nEnter your Aadhar Number: ')
    if len(str(aadhar_info))!=12:
        pprint("\nIncorrect Aadhar Number! Enter Valid aadhar of 12 digit!")
        aadhar_info = aadharCheck()
    return aadhar_info

# usernameCheck function takes the username from user & checks if it already exists in the database or not.
def usernameCheck():
    username_info = input('\nEnter your desired Username: ')
    query="select * from User where Username=%s"
    mycon= cur()
    user_query = (username_info,)
    mycon.execute(query,user_query)
    if(len(mycon.fetchall())>0):
        pprint("Username already Exist")
        username_info=usernameCheck()
    return username_info
