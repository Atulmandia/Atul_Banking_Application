from Benificiary import AddBeneficiary, viewBeneficiary
from Cards import Cards, ChangeMpin, NewCard
from Registeration import register
from Signin import signin
from Transaction import Transaction
from UpdateInfo import UpdateInfo
from ViewAccountBalance import viewAccountBalance

def select():
    """
        This function makes the user able to select the desired option they need to work on.
    """
    print("Select one option: ")

def wrongSelectedOptions(op1,op2):
    """
        This function will validate if the entry made by user is lying in the options or not.
        :param op1: Option 1 which is login().
        :param op2: Option 2 which is register().
    """
    print(f'\noption is wrong')
    selectedOption=int(input("\n Enter option number: "))
    SwitcherFunction(selectedOption,op1,op2)
    

def SwitcherFunction(argument,op1,op2):
    """
        This function will switch between functions.
        :param argument: It is the option entered by the user.
        :param op1: Option 1 which is login().
        :param op2: Option 2 which is register().
    """
    if argument==1:
        op1()
    elif argument==2:
        op2()
    elif argument==3:
        quit()
    else: wrongSelectedOptions(op1,op2)
    
def HomeOptions():
    """
        This function will display & take input from user regarding the options provided.
    """
    print("1. Login")
    print("2. Register Yourself")
    print("3. Exit")
    selectedOption=optionCheck()
    SwitcherFunction(selectedOption,signin,register)

def ProfileOptions(username):
    """
        This function will display all the options after successful login of the user.
        :param username: the username entered.
    """
    print("1. Account information")
    print("2. List of Beneficiaries")
    print("3. List of Cards")
    print("4. Add Beneficiary")
    print("5. Update Account information")
    print("6. Transfer Funds")
    print("7. Change MPIN")
    print("8. Register a New Credit or Debit Card")
    print("9. Exit")
    optionSelected= optionCheck()
    ProfileSwitcher(optionSelected,username,viewAccountBalance,viewBeneficiary,Cards,AddBeneficiary,UpdateInfo,Transaction,ChangeMpin,NewCard)

def WrongProfileOption(username,op1,op2,op3,op4,op5,op6,op7,op8):
    """
        This function will check if the entered option is right or wrong.
        :param username: the username entered.
        :param op1: Option 1 which is viewAccountBalance().
        :param op2: Option 2 which is viewBeneficiary().
        :param op3: Option 3 which is Cards().
        :param op4: Option 4 which is AddBeneficiary().
        :param op5: Option 5 which is UpdateInfo().
        :param op6: Option 6 which is Transaction().
        :param op7: Option 7 which is ChangeMpin().
        :param op8: Option 8 which is NewCard().
    """
    print(f'option is wrong\n')
    optionSelected=optionCheck()
    ProfileSwitcher(optionSelected,username,op1,op2,op3,op4,op5,op6,op7,op8)

def ProfileSwitcher(argument,username,op1,op2,op3,op4,op5,op6,op7,op8):
    """
        This function will switch between different functions based on the option selected.
        :param argument: It is the option entered by the user.
        :param username: the username entered.
        :param op1: Option 1 which is viewAccountBalance().
        :param op2: Option 2 which is viewBeneficiary().
        :param op3: Option 3 which is Cards().
        :param op4: Option 4 which is AddBeneficiary().
        :param op5: Option 5 which is UpdateInfo().
        :param op6: Option 6 which is Transaction().
        :param op7: Option 7 which is ChangeMpin().
        :param op8: Option 8 which is NewCard().
    """
    if argument==1:
        op1(username)
    elif argument==2:
        op2(username)
    elif argument==3:
        op3(username)
    elif argument==4:
        op4(username)
    elif argument==5:
        op5(username)
    elif argument==6:
        op6(username)
    elif argument==7:
        op7(username)
    elif argument==8:
        op8(username)
    elif argument==9:
        quit()
    else: WrongProfileOption(username,op1,op2,op3,op4,op5,op6,op7,op8)

def optionCheck():
    """
        This function will validate the entered option number. 
    """
    try : 
        enteredoption=int(input("\n Enter option number: "))
    except ValueError as ve:
        print(f'\nEntered value is not a number. Enter correct option.')
        enteredoption=optionCheck()
    return enteredoption