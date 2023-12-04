import sqlite3

import pandas as pd

df = pd.read_excel('products.xlsx')


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()
        self.create()
        self.populate_data()
        self.conn.commit()
        self.conn.close()
        
    def create(self):
        """Create a database file if it does not exist already"""
        return self.conn.execute("""CREATE TABLE IF NOT EXISTS Products(
          product_id INTEGER PRIMARY KEY,
          product_name text,
          product_price real
        )""")

    def populate_data(self):
      """Prepopulate the database"""
      for index, row in df.iterrows():
        self.cursor.execute('''
          INSERT INTO Products (product_name, product_price) VALUES (?, ?)
        ''',  (row['Product name'], row['Price']))
      print("Data populated")

db = Database()
