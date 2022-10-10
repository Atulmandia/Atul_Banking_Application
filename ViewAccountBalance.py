from pprint import  pprint

from MySQL_Connect import connect
from backToProfile import backToProfile

#viewAccountBalance function helps us to provide an option to display the account balance of the user.
def viewAccountBalance(username):
    connection=connect()
    cursor=connection.cursor(buffered=True)
    cursor.execute("select Account_balance from Account where Username=%s",(username,))
    balance=cursor.fetchone()
    pprint(f'Your Account Balance is {balance[0]}')
    backToProfile(username)