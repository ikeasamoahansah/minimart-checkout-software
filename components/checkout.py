import tkinter as tk
import sqlite3

from customtkinter import CTkToplevel, CTkLabel, CTkButton

class Checkout:

    def __init__(self, master):
        self.master = master
    
    def checkout(self):
        checkout_window = CTkToplevel(self.master)
        checkout_window.title("Checkout Window")

        checkout_list = tk.Listbox(checkout_window, width=40, height=10)
        checkout_list.pack()

        self.calculate_total_price(checkout_window)

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_price FROM Products")
        products = cursor.fetchall()
        conn.close()

        for product in products:
            checkout_list.insert(tk.END, f"{product[0]} - ${product[1]}")

    def calculate_total_price(self, window):
        total_price_label = CTkLabel(master=window, text="Total Price: ")
        total_price_label.pack(padx=5, pady=5)

        calculate_button = CTkButton(master=window, text="Calculate Total", command=lambda: self.calculate_total(window, total_price_label))
        calculate_button.pack(padx=20, pady=20)

    def calculate_total(self, checkout_list, total_price_label):
        total_price = 0

        for item in checkout_list.get(0, tk.END):
            price = float(item.split('$')[-1])
            total_price += price
        total_price_label.config(text=f"Total Price: ${total_price:.2f}")
