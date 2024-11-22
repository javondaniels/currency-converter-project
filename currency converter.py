import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0, 'EUR': 0.91, 'GBP': 0.79, 
            'JPY': 147.57, 'CAD': 1.35
        }
        
        self.window = tk.Tk()
        self.window.title('Currency Converter')
        self.window.geometry('350x400')
        self.window.configure(bg='#00008B')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        container = tk.Frame(self.window, bg='#00008B', padx=30, pady=20)
        container.pack(fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(
            container, 
            text='Currency Converter', 
            font=('Arial', 18, 'bold'), 
            bg='#00008B'
        ).pack(pady=10)
        
        # Amount input
        tk.Label(container, text='Amount:', bg='#00008B', fg='white').pack()

        self.amount = tk.Entry(container, justify='center', font=('Arial', 14))
        self.amount.pack(pady=10)
        self.amount.insert(0, '1')
        
        # Currency dropdowns
        self.from_curr = self.create_currency_dropdown(container, 'From:')
        self.to_curr = self.create_currency_dropdown(container, 'To:')
        
        # Convert button
        tk.Button(
            container, 
            text='Convert', 
            command=self.convert, 
            #bg='#4CAF50', 
            #fg='white', 
            font=('Arial', 12, 'bold')
        ).pack(pady=15)
        
        # Result display
        self.result = tk.Label(
            container, 
            text='', 
            font=('Arial', 14), 
            bg='#00008B',
            fg='white'
        )
        self.result.pack()
        
    def create_currency_dropdown(self, parent, label):
        tk.Label(parent, text=label, bg='#00008B', fg='white').pack()
        dropdown = ttk.Combobox(
            parent, 
            values=list(self.rates.keys()), 
            state='readonly', 
            width=15
        )
        dropdown.pack(pady=5)
        dropdown.set('USD' if label == 'From:' else 'EUR')
        return dropdown
        
    def convert(self):
        try:
            amount = float(self.amount.get())
            from_curr = self.from_curr.get()
            to_curr = self.to_curr.get()
            
            result = amount * (self.rates[to_curr] / self.rates[from_curr])
            
            self.result.config(
                text=f'{amount:.2f} {from_curr} = {result:.2f} {to_curr}'
            )
        except ValueError:
            self.result.config(text='Invalid input')
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    CurrencyConverter().run()