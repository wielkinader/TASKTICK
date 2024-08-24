import sqlite3

connection = sqlite3.connect("taskdb.db")
cursor = connection.cursor()


# This cuntion is used to show created tables within database
#res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

#This line is used to create a new table within the databse
#cursor.execute("CREATE TABLE tasksmain(id, title, progress)")

#This line is used to create a new table within the databse
#cursor.execute("CREATE TABLE IF NOT EXISTS tasksmain(title, progress)")