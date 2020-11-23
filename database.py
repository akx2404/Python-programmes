import sqlite3
myschool=sqlite3.connect('MyCricket.db')
curschool=myschool.cursor()
curschool.execute('''CREATE TABLE students (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT(20) NOT NULL,
house TEXT,
marks REAL);''')
myschool.close()
