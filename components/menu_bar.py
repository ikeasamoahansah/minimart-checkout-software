import tkinter as tk


class MenuBar:
    def __init__(self, master):
        self.master = master
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.master)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.file_new)
        file_menu.add_command(label="Open", command=self.file_open)
        file_menu.add_command(label="Save", command=self.file_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.file_exit)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=menu_bar)

    def file_new(self):
        print("New File Created")

    def file_open(self):
        print("File Opened!")

    def file_save(self):
        print("File Saved!")

    def file_exit(self):
        print("You quit!")
