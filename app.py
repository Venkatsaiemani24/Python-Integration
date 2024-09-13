import sqlite3
# Connecting to a database. if it doesn't exist,the database automatically created with the given name. 
connection = sqlite3.connect('LibrarySystem.db')
# Creating a cursor object to interact with the database.
cursor = connection.cursor()
# Creating a table library_books in LibrarySystem Database.
cursor.execute('''CREATE TABLE library_books (BookID INTEGER PRIMARY KEY, Title TEXT NOT NULL, Author TEXT NOT NULL, Genre TEXT, Availability TEXT CHECK(Availability IN('Yes','No')))''')
# Inserting record into the table.
cursor.execute("INSERT INTO library_books(Title,Author,Genre,Availability) VALUES('The Art of Computer Programming','Donald Knuth','Programming','Yes')")
# Using Parameters to prevent SQL injection attacks.
cursor.execute("INSERT INTO library_books(Title,Author,Genre,Availability) VALUES (?, ?, ?, ?)", ('A Brief History of Time','Stephen Hawking','Science','No'))
#Select all records from the table.
# creating Try-except block to aviod potiential Errors.
try:
 cursor.execute("SELECT *FROM library_books")
except sqlite3.OperationalError as e:
 print(f"An error occurred: {e}")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Commiting the changes.
connection.commit()
# Closing the Connection.
connection.close()