import configparser
import mysql.connector

file='pi.ini'
config= configparser.ConfigParser()
config.read('/home/nineleaps/Desktop/Banking_Application_ATUL/Atul_Banking_Application/pi.ini')

a=(config['Private']['host'])
b=(config['Private']['user'])
c=(config['Private']['password'])
d=(config['Private']['db'])

def connect():
    """
        This function establishes a connection between Python and MySQL
    """
    con= mysql.connector.connect(host=a,user=b,password=c,db=d)
    con.autocommit=True
    return con

def select():
    """
        This function makes the user able to select the desired option they need to work on.
    """
    print("Select one option: ")
    