import random
import re
from MySQL_Connect import connect
from Signin import signin
from execution import cur

def register():
    """
        This function start asking personal info of the user.
    """
    connection=connect()
    username= usernameCheck()
    name=nameCheck()
    address=addressCheck()
    aadhar = aadharCheck() 
    mobile = mobileCheck()
    password=checkPassword()
    query = "insert into User values (%s, %s, %s, %s, %s, %s)"
    mycon=connection.cursor()
    user_query = (username,name,aadhar,mobile,password,address,)
    mycon.execute(query,user_query)
    cursor1= connection.cursor(buffered=True)
    cursor1.execute("Select * from Account")
    cursor2=connection.cursor(buffered=True)
    cursor2.execute("insert into Account values(%s,%s,5000)",(cursor1.rowcount+100000000000+1,username,))
    
    #Here, we are allotting credit card to user after registration in which card number is generated randomly & simultaneously checked by check() function.
    cursor3=connection.cursor(buffered=True)
    cardNumber1=check(connection)
    pin1=random.randint(1000,9999)
    cvv1=random.randint(100,999)
    cursor3.execute("insert into Cards values(%s,%s,%s,%s,%s)",(cardNumber1,"Credit_card",pin1,cvv1,username,))
    
    #Here, we are allotting debit card to user after registration in which card number is generated randomly & simultaneously checked by check() function.
    cursor4=connection.cursor(buffered=True)
    cardNumber2=check(connection)
    pin2=random.randint(1000,9999)
    cvv2=random.randint(100,999)
    cursor4.execute("insert into Cards values(%s,%s,%s,%s,%s)",(cardNumber2,"Debit_card",pin2,cvv2,username,))

    print(f'\nRegistered Successfully! \n \n Login to Continue.')
    signin()

def check(connection):
    """
        This function will check if the cardnumber recently alloted does not lie in the already alloted cards.
        :param connection: This parameter is the establishment of connection to create a cursor & the function is called everywhere with "connection" only.
    """
    cursor=connection.cursor(buffered=True)
    cardnumber=random.randint(1000000000000000,9999999999999999)
    cursor.execute("select Card_number from Cards")
    cards=cursor.fetchall()
    while len(cards) and cardnumber in cards[0]:
        cardnumber=random.randint(1000000000000000,9999999999999999)
    return cardnumber

def nameCheck():
    """
        This function will not allow directly entering "enter" on the name entry.
    """
    name = input('\nEnter Your name: ')
    if len(name)==0:
        print(f'\nName cannot be empty. \nRe-Enter Your Name.') 
        name=nameCheck()
    return name

def addressCheck():
    """
        This function will not allow directly entering "enter" on the address entry.
    """
    address = input('\nEnter Your address: ')
    if len(address)==0:
        print(f'\nAddress cannot be empty. \nRe-Enter Your Address.') 
        address=addressCheck()
    return address

def mobileCheck():
    """
        This function takes the mobile number & checks the input if it is 10 digit or not.
    """
    try: 
        mobile_info = int(input(f'\nEnter your mobile number: +91-'))
    except ValueError as ve:
        print(f'Enter Valid Mobile Number!')
        mobile_info = mobileCheck()
    if len(str(mobile_info))!=10:
        print(f'Enter Valid Mobile Number!')
        mobile_info = mobileCheck()
    return mobile_info

def aadharCheck():
    """
        This function takes the aadhar number & checks the input if it is 12 digit or not.
    """
    try:
        aadhar_info = int(input(f'\nEnter your Aadhar Number: '))
    except ValueError as ve:
        print(f'Enter Valid Aadhar Number!')
        aadhar_info=aadharCheck()
    if len(str(aadhar_info))!=12:
        print(f'\nIncorrect Aadhar Number! Enter Valid aadhar of 12 digit!')
        aadhar_info = aadharCheck()
    return aadhar_info

def usernameCheck():
    """
        This function takes the username from user & checks if it already exists in the database or not.
    """
    print(f'Username must contain alphabets & numbers (NO SPECIAL CHARACTERS ALLOWED)\n')
    username_info = input('\nEnter your desired Username: ')
    if(valid_username(username_info)):
        print(f'\n Only Alphabets & Numbers are allowed in Username.')
        username_info=usernameCheck()
    query="select * from User where Username=%s"
    mycon= cur()
    user_query = (username_info,)
    mycon.execute(query,user_query)
    if(len(mycon.fetchall())>0):
        print("Username already Exist!")
        username_info=usernameCheck()
    return username_info

def valid_username(username):
    """
        This function validates the entered username, if the user doesn't follow the written requirements of the username input, this will ask to re-enter it.
        :param username: the username entered.
    """
    if not username.isalnum():
        return True
    return False

def checkPassword():
    """
        This function validates the entered password, if the user doesn't follow the written requirements of the password input, this will ask to re-enter it.
    """
    print(f'Password must contain atleast 1 uppercase, 1 lowercase & 1 special character\n')
    password = input('\nEnter password: ')
    if not ( re.search(r'\d', password) and
                re.search(r'[A-Z]', password) and
                re.search(r'[a-z]', password) and
                re.search(r'[@$!%*#?&]', password)):
                    password=checkPassword()
    return password    