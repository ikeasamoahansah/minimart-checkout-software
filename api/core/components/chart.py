import sqlite3

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()
cursor.execute("SELECT product_name, product_price FROM Products")
products = cursor.fetchall()
conn.close()


class Chart:
    def __init__(self, master) -> None:
        self.master = master
        self.create_chart(master, products)

    def create_chart(self, master, products):
        product_names = [product[0] for product in products]
        product_prices = [product[1] for product in products]

        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(product_names, product_prices)
        ax.set_xlabel("Products")
        ax.set_ylabel("Prices")
        ax.set_title("Product Prices")

        # Embed bar chart in TKinter window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)
