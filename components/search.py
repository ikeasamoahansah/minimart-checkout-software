import sqlite3
import tkinter as tk
from customtkinter import CTkEntry, CTkToplevel, CTkLabel, CTkButton

class Search:
    def __init__(self, master) -> None:
        self.search_results_listbox = None
        self.search_box(master)

    def search_box(self, master):
        search_window = CTkToplevel(master)
        search_window.title("Search Products")
        search_window.geometry("800x300")

        CTkLabel(search_window, text="Search Product:").pack()

        # Entry widget for user input
        search_entry = CTkEntry(search_window)
        search_entry.pack(pady=5)

        # Button to trigger the search
        search_button = CTkButton(search_window, text="Search", command=lambda: self.search_products(search_entry.get()))
        search_button.pack(pady=5)

        # Listbox to display search results
        self.search_results_listbox = tk.Listbox(search_window, width=40, height=10)
        self.search_results_listbox.pack(pady=20)

    def search_products(self, search_term):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Execute the search query
        cursor.execute("SELECT product_name, product_price FROM Products WHERE product_name LIKE ?", ('%' + search_term + '%',))
        search_results = cursor.fetchall()

        conn.close()

        # Display the search results in the listbox
        self.display_search_results(search_results)

    def display_search_results(self, search_results):
        # Clear the existing content in the listbox
        self.search_results_listbox.delete(0, tk.END)

        # Display the new search results in the listbox
        for result in search_results:
            self.search_results_listbox.insert(tk.END, f"{result[0]} - ${result[1]}")

