#!/usr/bin/env python3
############################################################
#######                                              #######
#######   Logic Implimentation for the Fire module   #######
#######                            by Ishan Saha     #######
#######                                              #######
############################################################

import sqlite3
import os 
import time
import requests

database = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Stats.db")
URL = "http://10.0.15.1"
Room_temperature = 27

def ConnectWIFI():
    """This function is to connect to different NODES for the fire module"""
    pass
def SMS(number, msg):
    """ A simple function to send SMS to the Owner and return True of False based on the response & and takes number and the message body as the arguements. """
    pass

def Call(number):
    """A simple function to call to the given number to notify the owner"""
    pass

def ReadSMS():
    """ A simple function to read the incoming sms and read 1.)name 2.)Number 3.)Address 4.)Location ."""
    Flag = False

    ### Read all the sms and dont change the flag 

    Name = Number = Address = Location = "testing"
    try:
        connection = sqlite3.connect(database)
        Cursor = connection.cursor()
        query = """INSERT INTO owner VALUES(?,?,?,?)"""
        Cursor.execute(query,(Name, Number, Address, Location))
        connection.commit()
        Cursor.exit()
        Flag = True
    except Exception as e:
        print(e)
    finally:
        return Flag

def fetchNumber():
    try:
        connection = sqlite3.connect(database)
        Cursor = connection.cursor()
        query = """SELECT name, number FROM owner LIMIT 1"""
        Cursor.execute(query)
        row = Cursor.fetchall()
        if len(row) is 0:
            return False
        else:
            return (row[0], row[1])
    except Exception as e:
        print(e)

if fetchNumber() is False:
    while True:
        if ReadSMS() is True:
            break

else:

    response = requests.get(URL)
    Temperature = response.json()['Temperature']
    Humidity = response.json()['Humidity']
    try:
        connection = sqlite3.connect(database)
        Cursor = connection.cursor()
        query = """INSERT INTO logs VALUES(?,?)"""
        Cursor.execute(query,(Temperature,Humidity))
        connection.commit()
        Cursor.exit()

        if Temperature>75:
            SMS(fetchNumber(),"Fire Alarm!")
            Call(fetchNumber())
    except:
        pass
