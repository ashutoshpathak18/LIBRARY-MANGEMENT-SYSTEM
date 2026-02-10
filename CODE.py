import mysql.connector
from datetime import date, datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
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

# Borrowing Functions

def borrow_book():
    member_id= int(input("Enter member ID :"))
    book_id= int(input("Enter book ID :"))
    borrow_date= date.today()
    cur.execute("insert into borrowings (member_id, book_id, borrow_date) values (%s,%s,%s)", (member_id,book_id,borrow_date))
    conn.commit()
    print("Book borrowed successfully...!")

def return_book():
    member_id= int(input("Enter member ID :"))
    book_id= int(input("Enter book ID :"))
    return_date= date.today()
    cur.execute("update borrowings set return_date=%s where member_id=%s and book_id=%s and return_date is NULL", (return_date,member_id,book_id))
    conn.commit()
    print("Book returned successfully...!")

def view_borrowings():
    cur.execute("select * from borrowings")
    borrowings=cur.fetchall()
    for borrowing in borrowings:
        print(f"ID: {borrowing[0]}, Member ID: {borrowing[1]}, Book ID: {borrowing[2]}, Borrow Date: {borrowing[3]}, Return Date: {borrowing[4]}")
    
# Close the connection when done

def close_connection():
    cur.close()
    conn.close()
    database="library"
    print("Connection closed....")

while(True):
    print("Welcome to the Library Management System\n")
    print("Press 1 for Librarian Registration")
    print("Press 2 for Librarian Login")
    print("Press 3 for Student Registration")
    print("Print 4 for Student Login")
    print("Press 5 to Exit")
    choice= int(input())

    choice= int(input())
    if choice==1:
        librarian_register()
    elif choice==2:
        if librarian_login():
            print("Librarian Login Successful....!")
            while(True):
                print("Press 1 to View Book")
                print("Press 2 to Add Books")
                print("Press 3 to Update Book")
                print("Press 4 to Delete Book")
                print("Press 5 to View Students")
                print("Press 6 to Add Student")
                print("Press 7 to Delete Student")
                print("Press 8 to View Borrowings")
                print("Press 9 to Logout")
                choice= int(input())
                if choice==1:
                    view_books()
                elif choice==2:
                    add_book()
                elif choice==3:
                    update_book()
                elif choice==4:
                    delete_book()
                elif choice==5:
                    view_members()
                elif choice==6:
                    member_register()
                elif choice==7:
                    delete_member()
                elif choice==8:
                    view_borrowings()
                elif choice==9:
                    break
                else:
                    print("Invalid Choice....!")
        else:
            print("Invalid Username or Password...!")
    
    elif choice==3:
        member_register()
        
    elif choice==4:
        if member_