import tkinter as tk
import sqlite3

from customtkinter import CTkToplevel, CTkLabel, CTkButton

# from payments.momo_pay import MobileMoney


class Checkout:
    def __init__(self, master):
        self.master = master

    def checkout(self):
        checkout_window = CTkToplevel(self.master)
        checkout_window.title("Checkout Window")
        checkout_window.geometry("800x400")

        checkout_list = tk.Listbox(
            checkout_window, width=40, height=10, selectmode=tk.MULTIPLE
        )
        checkout_list.pack()

        total_price_label = CTkLabel(checkout_window, text="Total Price: ")
        total_price_label.pack(padx=5, pady=5)

        calculate_button = CTkButton(
            checkout_window,
            text="Calculate Total",
            command=lambda: self.calculate_total(checkout_list, total_price_label),
        )
        calculate_button.pack(padx=20, pady=20)

        payment_button = CTkButton(checkout_window, text="Pay", command=self.pay_for())
        payment_button.pack(padx=20, pady=5)

        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_price FROM Products")
        products = cursor.fetchall()
        conn.close()

        for product in products:
            checkout_list.insert(tk.END, f"{product[0]} - ${product[1]}")

    def calculate_total(self, checkout_list, total_price_label):
        total_price = 0
        selected_indices = checkout_list.curselection()

        for index in selected_indices:
            item = checkout_list.get(index)
            price = float(item.split("$")[-1])
            total_price += price
        total_price_label.configure(text=f"Total Price: ${total_price:.2f}")

    def pay_for(self):
        return print("Request ongoing!")
