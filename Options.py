from pprint import  pprint
from Benificiary import AddBeneficiary, viewBeneficiary
from Cards import Cards, ChangeMpin, NewCard
from Registeration import register
from Signin import signin
from Transaction import Transaction
from UpdateInfo import UpdateInfo
from ViewAccountBalance import viewAccountBalance

# select function makes the user able to select the desired option they need to work on.
def select():
    pprint("Select one option: ")

#WrongSelectedOptions function will validate if the entry made by user is lying in the options or not
def wrongSelectedOptions(op1,op2):
    pprint("option is wrong")
    selectedOption=int(input("\n Enter option number: "))
    SwitcherFunction(selectedOption,op1,op2)
    
#SwitcherFunction will switch between functions
def SwitcherFunction(argument,op1,op2):
    # pprint(argument==1)
    if argument==1:
        op1()
    elif argument==2:
        op2()
    elif argument==3:
        quit()
    else: wrongSelectedOptions(op1,op2)
    
#HomeOptions function will display & take input from user regarding the options provided.
def HomeOptions():
    pprint("1. Login")
    pprint("2. Register Yourself")
    pprint("3. Exit")
    selectedOption=optionCheck()
    SwitcherFunction(selectedOption,signin,register)

#ProfilelOptions function will display all the options after successful login of the user.
def ProfileOptions(username):
    pprint("1. Account information")
    pprint("2. List of Beneficiaries")
    pprint("3. List of Cards")
    pprint("4. Add Beneficiary")
    pprint("5. Update Account information")
    pprint("6. Transfer Funds")
    pprint("7. Change MPIN")
    pprint("8. Register a New Credit or Debit Card")
    pprint("9. Exit")
    optionSelected= optionCheck()
    ProfileSwitcher(optionSelected,username,viewAccountBalance,viewBeneficiary,Cards,AddBeneficiary,UpdateInfo,Transaction,ChangeMpin,NewCard)

#WrongProfileOption function will check if the entered option is right or wrong.
def WrongProfileOption(username,op1,op2,op3,op4,op5,op6,op7,op8):
    pprint(f'option is wrong\n')
    optionSelected=optionCheck()
    ProfileSwitcher(optionSelected,username,op1,op2,op3,op4,op5,op6,op7,op8)

#Profileswitcher function will switch between different functions based on the option selected.
def ProfileSwitcher(argument,username,op1,op2,op3,op4,op5,op6,op7,op8):
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
    try : 
        enteredoption=int(input("\n Enter option number: "))
    except ValueError as ve:
        print(f'\nEntered value is not a number. Enter correct option.')
        enteredoption=optionCheck()
    return enteredoption