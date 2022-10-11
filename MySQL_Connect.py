import configparser
import mysql.connector
from pprint import pprint

file='pi.ini'
config= configparser.ConfigParser()
config.read('/home/nineleaps/Desktop/Banking_Application_ATUL/Atul_Banking_Application/pi.ini')

a=(config['Private']['host'])
b=(config['Private']['user'])
c=(config['Private']['password'])
d=(config['Private']['db'])

# connect function establishes a connection between Python and MySQL
def connect():
    con= mysql.connector.connect(host=a,user=b,password=c,db=d)
    con.autocommit=True
    return con

# select function makes the user able to select the desired option they need to work on.
def select():
    pprint("Select one option: ")
    