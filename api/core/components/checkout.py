import tkinter as tk
import sqlite3

from customtkinter import CTkToplevel, CTkLabel, CTkButton

from .payments.momo_pay import MobileMoney
from .search import Search


class Checkout:
    def __init__(self, master):
        self.master = master
        self.pricemsg = tk.StringVar()
        self.pricemsg.set("Total: 0")
        self.checkout(master)

    def checkout(self, master):
        checkout_window = CTkToplevel(master)
        checkout_window.title("Checkout Window")
        checkout_window.geometry("660x300")
        checkout_window.columnconfigure((0, 1, 2), weight=1)
        checkout_window.rowconfigure((0, 1, 2, 3), weight=1)

        checkout_list = tk.Listbox(
            checkout_window, width=20, height=10, selectmode=tk.MULTIPLE
        )
        checkout_list.grid(column=2, row=2)
        CTkLabel(checkout_window, text="Invoice/Checkout").grid(column=2, row=0, pady=5)

        total_price_label = CTkLabel(checkout_window, textvariable=self.pricemsg)
        total_price_label.grid(column=2, row=3, sticky="s", pady=5)

        checkout_list.bind(
            "<ButtonRelease-1>", lambda event: self.calculate_total(checkout_list)
        )
        Search(checkout_window)
        calculate_button = CTkButton(
            checkout_window,
            text="Pay",
            command=lambda: self.checkout_processing(checkout_list),
        )
        calculate_button.grid(column=1, row=3, sticky="s", pady=5, padx=5)

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_price FROM Products")
        products = cursor.fetchall()
        conn.close()

        for product in products:
            checkout_list.insert(tk.END, f"{product[0]} - ${product[1]}")

    def calculate_total(self, checkout_list):
        total_price = 0
        idx = checkout_list.curselection()
        for index in idx:
            item = checkout_list.get(index)
            price = float(item.split("$")[-1])
            total_price += price
        self.pricemsg.set(f"Total: {total_price}")

    def get_total(self, checkout_list):
        total_price = 0
        selected_indices = checkout_list.curselection()

        for index in selected_indices:
            item = checkout_list.get(index)
            price = float(item.split("$")[-1])
            total_price += price

        return total_price

    def checkout_processing(self, checkout_list):
        total_price = self.get_total(checkout_list)

        self.payment_processing(total_price)

    def payment_processing(self, price):
        m = MobileMoney()
        return m.pay(number="+233257262110", amount=f"{price}")
