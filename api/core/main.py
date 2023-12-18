import customtkinter
from layouts.menu_bar import MenuBar
from components.chart import Chart
import matplotlib.pyplot as plt


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x600")
        self.title("Minimart Checkout Software")
        self.button = customtkinter.CTkButton(
            self, text="Load Chart", command=self.load_chart
        )
        self.button.pack(padx=20, pady=20)
        self.bind("<Destroy>", self.on_destroy)

    def on_destroy(self, event):
        plt.close("all")

    def load_chart(self):
        Chart(self)


app = Main()
menu = MenuBar(app)
app.mainloop()
