import csv
import sqlite3

from colorama import Cursor

conn = sqlite3.connect('jarvis.db')

Cursor = conn.cursor()

# Path for system commands
#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(50),PATH varchar(1000))"
#Cursor.execute(query)

#query = "Insert into sys_command values(null,'VS Code','C:\\Users\piyus\.vscode\\Microsoft VS Code\\Code.exe')"
#Cursor.execute(query)
#conn.commit()


# Path for web commands
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name varchar(50),url varchar(1000))"
# Cursor.execute(query)
# query = "Insert into web_command values(null,'canva','https://www.canva.com/')"
# Cursor.execute(query)
# conn.commit()

# Path for applications automation
#table creation for contacts
# Cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         Cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()

# Insert Single contacts (Optional)
# query = "INSERT INTO contacts VALUES (null,'mummy', '7972762159',' ')"
# Cursor.execute(query)
# conn.commit()

# Delete Contacts from table 
# Cursor = conn.cursor(); Cursor.execute('DELETE FROM contacts');
# conn.commit(); 
# conn.close(); 
# print('All data deleted from contacts table.')

# #### Count Rows in contacts table
# Cursor.execute('SELECT COUNT(*) FROM contacts'); 
# result = Cursor.fetchone(); 
# print(f'Number of rows in contacts table: {result[0]}'); 
# conn.close()


#### Search Contacts from database
# query = 'papa'
# query = query.strip().lower()
# Cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = Cursor.fetchall()
# print(results[0][0])




