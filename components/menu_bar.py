import tkinter as tk
from customtkinter import CTkToplevel, CTkEntry, CTkButton
import matplotlib.pyplot as plt
import sqlite3


class MenuBar:
    def __init__(self, master):
        self.master = master
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.master)
        menu_bar.config(background="#808080")

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Add new", command=self.file_new)
        file_menu.add_command(label="Open", command=self.file_open)
        file_menu.add_command(label="Save", command=self.file_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.file_exit)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=menu_bar)

    def file_new(self):
        new_window = CTkToplevel(self.master)
        new_window.title("Add Products")
        new_window.geometry("300x150")

        product_name_entry = CTkEntry(new_window)
        product_price_entry = CTkEntry(new_window)
        product_name_entry.insert(0, 'Product name')
        product_price_entry.insert(0, 'Product price')
        product_name_entry.pack(pady=5)
        product_price_entry.pack(pady=5)

        save_button = CTkButton(new_window, text="Save", command=lambda: self.save_to_database(product_name_entry.get(), product_price_entry.get(), new_window))
        save_button.pack(pady=5)

    def file_open(self):
        print("File Opened!")

    def file_save(self):
        print("File Saved!")

    def file_exit(self):
        plt.close('all')
        self.master.quit()

    def save_to_database(self, name, price, window):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (product_name, product_price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()
        window.destroy()
        self.file_new()
