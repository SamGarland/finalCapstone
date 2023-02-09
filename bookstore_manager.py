'''This programme allows a user to access and manipulate a database 'ebookstore_db'.
The programme has the following parts:
    (1) Opens the database and creates a cursor object.
    (2) Attempts to create and fill the table 'books'. If the table already exists, this is skipped.
    (3) Lists a series of functions (enter_book, update_book, delete_book and search_book) that are 
        called in the user menu.
    (4) Gives an interactive user menu. 
'''

#===== EBOOKSTORE =====#

import sqlite3

#===== Opening the database =====#

datab = sqlite3.connect('ebookstore_db')

cursor = datab.cursor()

#===== Creating the table (if needed) =====#

try:

    cursor.execute('''CREATE TABLE IF NOT EXISTS books(Id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
    datab.commit()
    
    id_1 = 3001
    title_1 = "A Tale of Two Cities"
    author_1 = "Charles Dickens"
    qty_1 = 30
    
    id_2 = 3002
    title_2 = "Harry Potter and the Philosopher's Stone"
    author_2 = "J.K.Rowling"
    qty_2 = 40
    
    id_3 = 3003
    title_3 = "The Lion, the Witch and the Wardrobe"
    author_3 = "C.S.Lewis"
    qty_3 = 25
    
    id_4 = 3004
    title_4 = "The Lord of the Rings"
    author_4 = "J.R.R Tolkien"
    qty_4 = 37
    
    id_5 = 3005
    title_5= "Alice in Wonderland"
    author_5 = "Lewis Carroll"
    qty_5 = 12
    
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
    (id_1, title_1, author_1, qty_1))
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
    (id_2, title_2, author_2, qty_2))
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
    (id_3, title_3, author_3, qty_3))
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
    (id_4, title_4, author_4, qty_4))
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
    (id_5, title_5, author_5, qty_5))
     
    datab.commit()
    print("A new table 'Books' has been created.")

except sqlite3.Error as table_exists:
    print("\nAccessing your database 'ebookstore_db' and tables.\n")

#===== The Database Manager =====#

print("Hello! Welcome to bookstore database manager.")

#===== Functions =====#

def enter_book():
    
    print("\nYou've have selected: 'Enter book'\n")
        
    new_book_id = input("Please enter the new book's id number:\n")
    new_book_id = int(new_book_id)
    new_book_title = input("And what is the title?\n")
    new_book_author = input("Who is the author?\n")
    new_book_qty = input("Finally, what quantity are there?")
    new_book_qty = int(new_book_qty)
    
    cursor.execute('''INSERT INTO books(Id, Title, Author, Qty) VALUES (?, ?, ?, ?)''', 
                   (new_book_id, new_book_title, new_book_author, new_book_qty))
    
    datab.commit()
    print("That book has been added successfully.")
    
def update_book():
    
    print("\nYou've have selected: 'Update book'\n")
        
    select_by_id = input("What is the id of the book you want to update?")
    
    select_by_id = int(select_by_id)
    
    while True:
        
        user_updates = input('''What information would you like to update?
(1) Id
(2) Title
(3) Author
(4) Quantity
(0) Back to main menu
:''')

        try:
            
            user_updates.strip()
            user_updates = int(user_updates)
    
            if user_updates == 1:
                
                update_id = input("Please enter the new Id:")
                update_id = int(update_id)
                
                cursor.execute('''UPDATE books SET Id = ? WHERE Id = ?''', 
                               (update_id, select_by_id))
                print("\nThat has been updated.\n")
                
            elif user_updates == 2:
                
                update_title = input("Please enter the new title:")
                
                cursor.execute('''UPDATE books SET Title = ? WHERE Id = ?''', 
                               (update_title, select_by_id))
                
                print("\nThat has been updated.\n")
                
            elif user_updates == 3:
                
                update_author = input("Please enter the new author:")
                
                cursor.execute('''UPDATE books SET Author = ? WHERE Id = ?''', 
                               (update_author, select_by_id))
                
                print("\nThat has been updated.\n")
                
            elif user_updates == 4:
                
                update_qty = input("Please enter the new Quantity:")
                
                update_qty = int(update_qty)
                
                cursor.execute('''UPDATE books SET Qty = ? WHERE Id = ?''', 
                               (update_qty, select_by_id))
                
                print("\nThat has been updated.\n")
                
            elif user_updates == 0:
                break
            else:
                print("\nSorry, I didn't get that, please try again.\n")
        
            datab.commit()
        
        except ValueError:
            print("Sorry, that wasn't one of the options. Try again...")
            continue

def delete_book():
    
    try:
        
        user_delete = input("\nPlease enter the Id of the book you want to delete:\n")
            
        user_delete = int(user_delete)
    
        cursor.execute('''DELETE FROM books WHERE Id = ?''', (user_delete,))
        
        print("That book has been deleted.")
        
        datab.commit()
    
    except ValueError:
        print("Sorry, that wasn't a valid entry...")
    
def search_book():
    
    try:
    
        search_book = input("\nPlease enter the Id of the book you would like to view:\n")
            
        search_book = int(search_book)
        
        cursor.execute('''SELECT * FROM books WHERE Id = ?''', (search_book,))
        
        book = cursor.fetchall()
        
        for attr in book:
            print(f"\n{attr}\n")
    
    except ValueError:
        print("Sorry, that wasn't a valid entry...")

#===== User Menu =====#

while True:
    
    user_choice =  input('''Enter one of the following options:
(1) Enter book
(2) Update book
(3) Delete book
(4) Search book
(0) Exit
:''')

    try:
    
        user_choice.strip()
        user_choice = int(user_choice)
        
        if user_choice == 1:
            
            enter_book()
        
        elif user_choice == 2:
            
            update_book()
        
        elif user_choice == 3:
            
            delete_book()
        
        elif user_choice == 4:
            
            search_book()
        
        elif user_choice == 0:
            
            print("Your sqlite connect is closed.")
            print("\nGoodbye!\n")
            break
            datab.close()
        
        else:
            print("\nSorry, that's not one of the options! Please try again.\n")
    
    except ValueError:
        print("Sorry, that wasn't a valid entry. Try again.")   