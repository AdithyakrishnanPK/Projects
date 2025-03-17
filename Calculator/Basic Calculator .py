import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.configure(bg="#1e1e1e")

        self.expression = ""

        self.create_widgets() 

    def create_widgets(self):
        
        self.display = tk.Entry(
            self,
            font=("Arial", 24, "bold"),
            bg="#333333",
            fg="#ffa500",
            bd=5,
            justify="right",
            relief="flat",
            insertbackground="#ffa500"
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

      
        button_frame = tk.Frame(self, bg="#1e1e1e")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]

        button_styles = {
            "font": ("Arial", 18, "bold"),
            "relief": "flat",
            "bd": 0,
            "fg": "#ffa500",
            "activeforeground": "#1e1e1e",
            "activebackground": "#ffa500",
        }

        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#1e1e1e")
            row_frame.pack(fill=tk.BOTH, expand=True)

            for btn_text in row:
                button = tk.Button(
                    row_frame,
                    text=btn_text,
                    command=lambda b=btn_text: self.on_button_click(b),
                    bg="#333333",
                    **button_styles
                )
                button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += char

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
