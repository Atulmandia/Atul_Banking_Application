import random
from Registeration import check
from Transaction import CardType
from MySQL_Connect import connect
from backToProfile import backToProfile

def Cards(username):
    """
        This function will let us show the list of cards a person have or added to his account.
        This list of cards will contain the "Card Number", "card type" & "CVV" of the cards in the list.
        :param username: the username entered.
    """
    connection = connect()
    cursor= connection.cursor(buffered=True)
    cursor.execute("select * from Cards where Username=%s ",(username,))
    result=cursor.fetchall()
    cardNumbers=[row[0] for row in result]
    cardTypes=[row[1] for row in result]
    Pins=[row[2] for row in result]
    cvvs=[row[3] for row in result]
    i=1
    for(cardNumber,cardType,Pin,cvv) in zip(cardNumbers,cardTypes,Pins,cvvs):
        print(i)
        print(f'Card Number is {cardNumber}')
        print(f'Card Type is {cardType}')
        print(f'MPIN is {Pin}')
        print(f'CVV is {cvv}')
        i+=1
    backToProfile(username)
  
def ChangeMpin(username):
    """
        This function will allow user to change the PIN for his/her cards.
        :param username: the username entered.
    """
    cardNumber=int(input("Enter Card Number for PIN change: "))
    mpin=int(input("Enter the old MPin: "))
    connection = connect()
    cursor= connection.cursor(buffered=True)
    cursor.execute("select * from Cards where Card_number=%s and Pin=%s and Username=%s",(cardNumber,mpin,username,))
    result=cursor.fetchone
    if cursor.rowcount<1:
        print("Please, Enter correct card number & PIN.")
        ChangeMpin(username)
    else:
        newPin=int(input("Enter New Mpin: "))
        cursor2=connection.cursor()
        cursor2.execute("update Cards set Pin=%s where Card_number=%s",(newPin,cardNumber))
        print("MPIN Successfully changed!!")
    backToProfile(username)

def NewCard(username):
    """
        This function will allow user to register a new card.
        :param username: the username entered.
    """
    connection=connect()
    cursor=connection.cursor(buffered=True)
    print("Select your Card Type \n 1. Credit Card  2. Debit Card")
    selectedOption=int(input())
    CardTyped=CardType(selectedOption)
    cardNumber=check(connection)
    pin1=random.randint(1000,9999)
    cvv1=random.randint(100,999)
    cursor.execute("insert into Cards values(%s,%s,%s,%s,%s)",(cardNumber,CardTyped,pin1,cvv1,username,))
    print(f'\nNew card added to your account.\n')
    print(f'Your Card Number is: {cardNumber}')
    print("You can check your PIN in List of Cards.")
    backToProfile(username)