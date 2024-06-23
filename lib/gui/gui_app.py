import tkinter as tk

class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('PiNet-Manager')

        self.create_widgets()

    def create_widgets(self):
        # Create GUI widgets here
        pass

    def run(self):
        self.root.mainloop()
