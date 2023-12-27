import sqlite3
import tkinter as tk

from customtkinter import CTkEntry, CTkLabel


class Search:
    def __init__(self, master) -> None:
        self.search_results_listbox = None
        self.search_box(master)

    def search_box(self, master):
        CTkLabel(master, text="Search Product:").grid(column=0, row=0, pady=5, padx=10)

        # Entry widget for user input
        search_entry = CTkEntry(master)
        search_entry.grid(column=0, row=0, columnspan=2, pady=5)
        search_entry.bind(
            "<Return>", lambda event: self.search_products(search_entry.get())
        )

        # Listbox to display search results
        self.search_results_listbox = tk.Listbox(master, width=40, height=10)
        self.search_results_listbox.grid(column=0, row=2, columnspan=2)
        self.search_results_listbox.bind(
            "<ButtonRelease-1>",
            lambda event: self.add_to_invoice(self.search_results_listbox),
        )

    def add_to_invoice(self, box):
        selected_index = box.curselection()
        if selected_index:
            selected_item = box.get(selected_index[0])

            return selected_item

    def search_products(self, search_term):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        # Execute the search query
        cursor.execute(
            "SELECT product_name, product_price FROM Products WHERE product_name LIKE ?",
            ("%" + search_term + "%",),
        )
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
