import sqlite3

conn = sqlite3.connect('toydb.db')
cursor = conn.cursor()

# Retrieve data from customers table
cursor.execute("SELECT * FROM customers")
customers = cursor.fetchall()

# Retrieve data from orders table
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

# Close the connection
conn.close()
