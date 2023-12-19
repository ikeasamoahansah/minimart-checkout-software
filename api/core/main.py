import tkinter as tk
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
        self.lf = tk.LabelFrame(
            self,
            text="Chart Pane"   
        )
        self.lf.config(
            background="#303234",
            foreground="#FFF",
            width=700,
            height=600
        )
        self.lf.pack(padx=50, pady=50)
        self.bind("<Destroy>", self.on_destroy)

    def on_destroy(self, event):
        plt.close("all")

    def load_chart(self):
        Chart(master=self.lf)


if __name__ == "__main__":
    app = Main()
    menu = MenuBar(app)
    app.mainloop()
    
