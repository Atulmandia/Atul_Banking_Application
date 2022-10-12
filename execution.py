from multiprocessing import connection
from MySQL_Connect import connect
connection=connect()

def cur():
    """
        This function helps us to make SQL query run
    """
    return connection.cursor()