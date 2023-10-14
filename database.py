import sqlite3

# Connect to a database
conn = sqlite3.connect('minimart.db')

# Create a cursor
c = conn.cursor()

# Create DB Table
c.execute("""CREATE TABLE products(
          product_name text,
          product_price real,
          product_barcode integer
)""")

# Commit changes
conn.commit()

# CLose connection
conn.close()

