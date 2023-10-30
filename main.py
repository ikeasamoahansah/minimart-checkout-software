import customtkinter


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Minimart Checkout Software")
        self.button = customtkinter.CTkButton(self, text="Print receipt", command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("Button clicked")

app = Main()
app.mainloop()
