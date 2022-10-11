## Atul_Banking_Application
This is a Banking application project which includes basic operations done in a bank. This project is done on Python (in VS Code)

## This project needs the following tables:
1. "Account" table: Columns: (Account_number, Username, Account_balance) 
    - (PRIMARY KEY: "Account_number")
    - (FOREIGN KEY: "fk_Username", REFERENCED TABLE: "User", REFERENCED COLUMN: "Username")
    - This table will store account numbers, usernames & account balance for that particular account.
2. "Beneficiary" table: Columns: (BeneID, Name, Account_number, IFSC, Username)
    - (PRIMARY KEY: "BeneID")
    - (FOREIGN KEY: "fk_beneuser", REFERENCED TABLE: "User", REFERENCED COLUMN: "Username")
    - This table will be updated and will store beneficiary accounts added by the user.
3. "Cards" table: Columns: (Card_number, Card_type, Pin, CVV, Username)
    - (PRIMARY KEY: "Card_number")
    - (FOREIGN KEY: "fk_Cards_1", REFERENCED TABLE: "User", REFERENCED COLUMN: "Username")
    - This table contains all the cards alloted and registered by and for the user. In my code, I am providing both the credit & debit cards to the user       when he/she registers.
4. "Transactions" table: Columns: (TransactionID, Amount_value, From_Account, To_Account, Balance_left, Card_number, Date, IFSC, Recipient_name)
    - (PRIMARY KEY: "TransactionID")
    - (FOREIGN KEY1: "fk_card", REFERENCED TABLE: "Cards", REFERENCED COLUMN: "Card_number")
    - (FOREIGN KEY2: "fk_fromacc", REFERENCED TABLE: "Account", REFERENCED COLUMN: "Account_number")
    - This table gets updated whenever a transfer of fund is happened. In my code, If the transaction is from our bank account to our bank account, then         it'll show two transactions.
5. "User" table: Columns: (Username, Name, Aadhar_Number, Mobile_number, Password, Address)
    - (PRIMARY KEY: "Username")
    - (FOREIGN KEY: No Foreign Keys)
    - This table contains all the personal details of the user which he/she enters while registering themselves. 
    
## My code contains following files:
1. "Home.py" file is the main file which will connect rest of the files and functions to make the banking work. 
    - HomeOptions()- This function will display & take input from user regarding the options provided.
2. "MySQL_connect", "execution" & "Pi(copy)" files collectively sets up the connection between Python & MySQL. Please NOTE that the "pi(copy).ini" file contains dummy login credentials which must be changed according to your workbench login credentials.
    - "pi(copy).ini" file contains your username, password & other details required to login into MySQL Workbench.
    - "MySQL_connect.py" file will use "pi(copy).ini" to establish a connection between Python & MySQL Workbench.
    - "Execution.py" file let us run a SQL query in Workbench by creating a cursor.
3. "Registeration.py" file works around registeration of a new user and takes input from the user regarding his/her personal details to open a account and drops the user back to login page.
4. "backToProfile.py" file creates a back option, which when called takes the user to login options.
5. "Beneficiary.py" file contains 2 functions: 
    - AddBeneficiary()- this function allows user to add beneficiary accounts to his/her account.
    - viewBeneficiary()- this function allows user to be able to see the list of beneficiaries added to his account.
6. "Cards.py" file contains 3 functions:
    - Cards()- this function will let us show the list of cards a person have or added to his account.
    - ChangeMpin()- this function will allow user to change the PIN for his/her cards.
    - NewCard()- this function will allow user to register a new card.
7. "Options.py" file contains 7 functions:
    - Select()- this function makes the user able to select the desired option they need to work on.
    - wrongSelectedOptions()- this function will validate if the entry made by user is lying in the options or not.
    - SwitcherFunction()- this will switch between functions based on the option selected by the user.
    - HomeOptions()- this function will display & take input from user regarding the options provided.
    - ProfileOptions()- this function will display all the options after successful login of the user.
    - WrongProfileOption()- this function will check if the entered option is right or wrong.
    - ProfileSwitcher()- this function will switch between different functions based on the option selected.
8. "Signin.py" file contains a function "signin()" which will take input as username & password and validates them after the entries are made.
9. "Transaction.py" file contains 2 functions:
    - Transactions()- this function helps to do all the necessary validations, addition, subtraction & entries of transactions.
    - Cardtype()- this function will take evaluate and switch transaction through credit & debit card and at the same time checks the entered card             number whether it is wrong or right.
10. "UpdateInfo.py" file contains "UpdateInfo()" function which provides an option to update user information like name, mobile number & address.
11. "ViewAccountBalance.py" file contains "viewAccountBalance()" function which helps us to provide an option to display the account balance of the user.

# "Home.py" file runs the final code which calls the function "HomeOptions()"
