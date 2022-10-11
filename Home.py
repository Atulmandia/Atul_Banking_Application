from pprint import pprint
from MySQL_Connect import select
from Options import HomeOptions
from Registeration import check, register
from MySQL_Connect import select, connect
pprint("Welcome to ABC Bank")
#IFSC="ATUL000011"
connection=connect()
HomeOptions()
# pprint(check(connection))