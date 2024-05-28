import tkinter as tk
from tkinter import ttk
import math

class ForwardPrice:
    def __init__(self):
       pass

    def Physical_Commodities(self, C, t, r, s, i):
         self.C = C  # commodity price
         self.t = t  # time to maturity of the forward contract
         self.r = r  # interest rate
         self.s = s  # storage cost
         self.i = i  # annual insurance
         result = self.C * (1 + self.r/100 * self.t/12) + (self.s * self.t/12) + (self.i * self.t/12)
         return result

    def Stock(self, S, r, d, t):
        self.S=S#spot price
        self.r=r#intrest rates
        self.d=d# 
        self.t=t
        result =self.S*math.exp((self.r/100 - self.d/100) * self.t/12)
        return result

    def bond(self, B, r, c, t):
        self.B=B
        self.r = r / 100
        self.c = c / 100
        self.t = t / 12
        result = self.B * (1 + (self.r - self.c) * self.t)
        return result

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Screen")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Forward Price Calculator", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.button1 = tk.Button(self, text="Physical Commodities", command=lambda: self.open_new_screen("Physical Commodities"))
        self.button1.pack(pady=5)
        
        self.button2 = tk.Button(self, text="Stock", command=lambda: self.open_new_screen("Stock"))
        self.button2.pack(pady=5)
        
        self.button3 = tk.Button(self, text="bond", command=lambda: self.open_new_screen("bond"))
        self.button3.pack(pady=5)

    def open_new_screen(self, formula_type):
        if formula_type == "Physical Commodities":
            input_labels = ["Commodity price", "Time to maturity (in decimal)", "Interest rate", "Storage cost", "Annual insurance cost"]
        elif formula_type == "Stock":
            input_labels = ["Spot price (S)", "Risk-free rate (%) (r)", "Dividend yield (%) (d)", "Time to maturity in years (t)"]
        elif formula_type == "bond":
             input_labels = ["Bond price (B)", "Interest rate (%) (r)", "Coupon rate (%) (c)", "Time to maturity in months (t)"]
        NewScreen(self, formula_type, input_labels)

class NewScreen(tk.Toplevel):
    def __init__(self, parent, formula_type, input_labels):
        super().__init__(parent)
        self.title(f"New Screen - {formula_type}")
        self.geometry("400x400")
        
        self.inputs = []
        for i, label_text in enumerate(input_labels):
            label = tk.Label(self, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.inputs.append(entry)
        
        self.output_label = tk.Label(self, text="Output")
        self.output_label.grid(row=len(input_labels), column=0, padx=10, pady=5)
        self.output = tk.Label(self, text="", bg="white", width=20)
        self.output.grid(row=len(input_labels), column=1, padx=10, pady=5)
        
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=len(input_labels)+1, column=0, columnspan=2, pady=20)

        self.calculation = ForwardPrice()
        self.formula_type = formula_type

    def calculate(self):
        try:
            inputs = [float(entry.get()) for entry in self.inputs]
        except ValueError:
            self.output.config(text="Invalid input")
            return

        if self.formula_type == "Physical Commodities":
            result = self.calculation.Physical_Commodities(*inputs)
        elif self.formula_type == "Stock":
            result = self.calculation.Stock(*inputs)
        elif self.formula_type == "bond":
            result = self.calculation.bond(*inputs)
    
        self.output.config(text=str(result))




if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
