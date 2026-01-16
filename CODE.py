import mysql.connector
from datetime import date, datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="librarys"
)
cur=conn.cursor()

#Librarian Functions

def librarian_register():
    u = input("Enter username :")
    p = input("Enter password :")
    cur.execute("insert into librarian (username,password) values (%s,%s)", (u,p))
    conn.commit()
    print("Librarian registered successfully")

def librarian_login():
    u= input("Enter username :")
    p= input("Enter the password :")
    cur.execute("select * from librarian where username=%s and password=%s", (u,p))
    return cur.fetchone() is not None


# Book Functions
def add_book():
    name= input("Enter book name :")
