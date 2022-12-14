from MySQL_Connect import connect

def signin():
    """
        This function will take input as username & password and validates them after the entries are made.
    """
    print(f'--------WELCOME TO LOGIN PAGE--------\n')
    print(f'Enter the following details: \n')
    username=input("Enter your Username : ")

    #Below code will check the username entered if it is correct or not. 
    #If it is incorrect then it'll ask user to enter the correct one.
    #Also, there will be only 4 attempts to make it right.
    connection=connect()
    cursor=connection.cursor(buffered=True)
    cursor.execute("select Username from User")
     
    i=4
    my_result=cursor.fetchall()
    while username not in [row[0] for row in my_result]:
        i-=1
        if i<1:
            break
        username=input(f'\nUsername not found, {i} attempts left \nEnter correct Username : ')

    #Below code will check the entered password if it is correct or not. 
    #If it is incorrect then it'll ask user to enter the correct one.
    #Also, there will be only 4 attempts to make it right.    
    cursor1=connection.cursor(buffered=True)
    cursor1.execute("select Password from User where Username=%s ",(username,))
    passwordForCheck=cursor1.fetchone()[0]
    passwordInput=input('Enter your password : ')
    j=4
    while passwordForCheck != passwordInput:
        j-=1
        if(j<1):
            quit()
        passwordInput=input(f'\nPassword Incorrect, {j} attempts left \nEnter correct password again : ')
    if passwordForCheck==passwordInput:
        print(f'\n{username} Successfully Signed In! \n')
        print(f'\nSelect One option from below: ')
        import Options
        Options.ProfileOptions(username)