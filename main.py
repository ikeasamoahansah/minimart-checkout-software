import customtkinter
from components import menu_bar
from components.checkout import Checkout


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Minimart Checkout Software")
        self.checkout = Checkout(self)
        self.button = customtkinter.CTkButton(self, text="Checkout", command=self.checkout.checkout)
        self.button.pack(padx=20, pady=20)


app = Main()
menu = menu_bar.MenuBar(app)
app.mainloop()
