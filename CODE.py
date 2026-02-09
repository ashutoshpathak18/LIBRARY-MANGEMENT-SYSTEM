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
    author= input("Enter author name :")
    quantity= int(input("Enter quantity :"))
    cur.execute("insert into books (name,author,quantity) values (%s,%s,%s)", (name,author,quantity))
    conn.commit()

    print("Book added successfully....!")

def view_books():
    cur.execute("select * from books")
    books= cur.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

def update_book():
    book_id= int(input("Enter book ID to Update :"))
    name= input("Enter new book name :")
    author= input("Enter the new author name :")
    quantity= int(input("Enter new quantity :"))
    cur.execute("update books set name=%s, author=%s, quantity=%s, where id=%s", (name,author,quantity,book_id))
    conn.commit()
    print("Book update successfully....!")

def delete_book():
    book_id= int(input("Enter book ID to delete :"))
    cur.execute("delete from books where id=%s", (book_id,))
    conn.commit()
    print("Book deleted successfully.....!")

# Member Functions

def member_register():
    name= input("Enter member name :")
    email= input("Enter member Email :")
    cur.execute("insert into members (name,email) values (%s,%s)", (name,email))
    conn.commit()
    print("Member registered succcessfully...!")

def view_members():
    cur.execute("select * from members")
    members = cur.fetchall()
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")

def delete_member():
    member_id= int(input("Enter member ID to delete :"))
    cur.execute("delete from members where id=%s", (member_id,))
    conn.commit()
    print("Member deleted successfully...!")

