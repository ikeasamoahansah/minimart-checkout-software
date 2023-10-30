import sqlite3

import pandas as pd

FILE_NAME = 'data.xls'
df = pd.read_excel(FILE_NAME)


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.create()
        self.populate_data()
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.conn.close()
        
    def create(self):
        return self.conn.execute("""CREATE TABLE IF NOT EXISTS Products(
          product_id INTEGER PRIMARY KEY,
          product_name text,
          product_price real
        )""")

    def populate_data(self):
        for index, row in df.iterrows():
            self.cursor.execute("""
          INSERT INTO Products (product_name, product_price) VALUES (?, ?)
        """, (row['Product name'], row['Price']))
        print("data successfully imported")
    

db = Database()
