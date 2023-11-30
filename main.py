import customtkinter
from components import menu_bar
from components.checkout import Checkout
from components.chart import Chart
import matplotlib.pyplot as plt



class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x600")
        self.title("Minimart Checkout Software")
        self.checkout = Checkout(self)
        self.chart = Chart(self)
        self.button = customtkinter.CTkButton(self, text="New Checkout", command=self.checkout.checkout)
        self.button.pack(padx=20, pady=20)
        self.bind("<Destroy>", self.on_destroy)
    
    def on_destroy(self, event):
        plt.close('all')


app = Main()
menu = menu_bar.MenuBar(app)
app.mainloop()
