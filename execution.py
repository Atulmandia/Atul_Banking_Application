from multiprocessing import connection
from MySQL_Connect import connect
connection=connect()

# cur function helps us to make SQL query run
def cur():
    return connection.cursor()