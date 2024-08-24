#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect("taskdb.db")
cursor = connection.cursor()


# This line ensures the table is created if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasksmain(title, progress)")

from datetime import datetime
from functions import *
from ascart import taskticklogo, standinggiraffe
from colorama import init, Fore, Style

init()

# Get the current date
now = datetime.now()

# Format the date as 'Aug 23 2024'
formatted_date = now.strftime("%b %d %Y")

#This is to display the logo when the program is launched
taskticklogo()

while True:
    usrinput = input("What would you like to do? (type 'help' for list of commands)")
    
    if usrinput == 'add' or usrinput == 'a':
        add()
    elif usrinput == 'help' or usrinput == 'h':
        help()    
    elif usrinput == 'progress' or usrinput =='prog' or usrinput == 'p':
        progress()
    elif usrinput =='quit' or usrinput == 'q':
        print("Thanks for using TASCKTICK!")
        standinggiraffe()
        break
    elif usrinput =="tick" or usrinput == 't':
        progress()
        tick()
        progress()
    elif usrinput == "clear"or usrinput == 'c':
        clear()
        progress()
    elif usrinput == "clearall" or usrinput == "ca" or usrinput == 'clear all':
        clearall()
    else:
        print(Fore.YELLOW, 'Invalid Input')
