import sqlite3

from odf.opendocument import load

odf_file = 'data.odt'
doc = load(odf_file)


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()
        self.create()
        self.populate_data()
        self.conn.commit()
        self.conn.close()
        
    def create(self):
        return self.conn.execute("""CREATE TABLE IF NOT EXISTS Products(
          product_id INTEGER PRIMARY KEY,
          product_name text,
          product_price real
        )""")

    def populate_data(self):
      for sheet in doc.spreadsheet.getElementsByType("table:table"):
          for row in sheet.getElementsByType("table:table-row")[1:]:
              data = [cell.firstChild.data for cell in row.getElementsByType("table:table-cell")]
              self.cursor.execute("""
                INSERT INTO Products (product_name, product_price) VALUES (?,?)
              """, (data[0], float(data[1])))
          print("Data imported successfully")
    

db = Database()
