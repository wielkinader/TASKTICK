import sqlite3
from sqldb import *
from colorama import init, Fore, Style


init()

def add():
    addtask = input('What would you like to call your new task? ').lower()

    """
    with open('tasks.txt', 'a') as file:
        file.write('0' + " "+ addtask +  '\n')
    """

    cursor.execute("INSERT INTO tasksmain (title, progress) VALUES (?, '0')", (addtask,))
    connection.commit()
    print('Done!')



def help():
    print("\nThe 'add' command allows you to create a new task")
    print("The 'tick' command allows you to tick off tasks")
    print("The 'progress' command allows you to check the progress of any ongoing task")
    print("The 'clear' command allows you to remove all completed tasks from the database\n")
    print(Fore.RESET)

    


def progress():
    #used to check the progress of any task
    print('Current Progress of Tasks:')
   
    tasks = cursor.execute("SELECT * FROM tasksmain")
    for task in tasks:
        if task[1] == '0':
                print(Fore.RED, task[0].strip() + ' - In Progress')
        elif task[1] == '1':
                print(Fore.GREEN,task[0].strip() + ' - Completed')
    print(Fore.RESET)

def tick():
    task_name = input("What task have you completed? ").lower()
    cursor.execute("UPDATE tasksmain SET progress = '1' WHERE title = ?", (task_name,)) 
    connection.commit()

    cursor.execute("SELECT progress FROM tasksmain WHERE title = ?", (task_name,))
    progStatus = cursor.fetchone()
    print(Fore.RESET)



def clear():
    cursor.execute("DELETE FROM tasksmain WHERE progress ='1'")
    connection.commit()
    print(Fore.RESET)

     

def clearall():
    cursor.execute("DELETE FROM tasksmain")
    connection.commit()
    print(Fore.RESET)
