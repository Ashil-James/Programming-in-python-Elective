from breezypythongui import EasyFrame
from tkinter import ttk  # This imports the modern Tkinter tools (like Dropdowns)

class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Unit Converter", width=300, height=200)
        
        # 1. Input Field
        self.addLabel(text="Value: ", row=0, column=0)
        self.input = self.addTextField(text="", row=0, column=1)
        
        units = ["m", "km", "g", "kg", "ml", "l"]
        
        # 2. "From" Dropdown (Using standard ttk.Combobox)
        self.addLabel(text="From: ", row=1, column=0)
        self.fromUnit = ttk.Combobox(self, values=units, state="readonly", width=17)
        self.fromUnit.grid(row=1, column=1, padx=5, pady=5) # Place it in Breezy's grid
        self.fromUnit.set("m") # Set default visible value
        
        # 3. "To" Dropdown
        self.addLabel(text="To: ", row=2, column=0)
        self.toUnit = ttk.Combobox(self, values=units, state="readonly", width=17)
        self.toUnit.grid(row=2, column=1, padx=5, pady=5)
        self.toUnit.set("m") 
        
        # 4. Button & Output
        self.addButton(text="Convert", row=3, column=0, columnspan=2, command=self.convert)
        self.output = self.addLabel(text="Result: ", row=4, column=0, columnspan=2)
        
    def convert(self):
        try:
            val = float(self.input.getText()) 
            
            # Conversion factors relative to base units
            factors = {"m": 1, "km": 1000, "g": 1, "kg": 1000, "ml": 0.001, "l": 1}
            
            # NOTE: Comboboxes use .get() instead of .getSelectedItem()
            f = self.fromUnit.get()
            t = self.toUnit.get()
            
            # Define compatible categories
            dist = ["m", "km"]
            mass = ["g", "kg"]
            vol = ["ml", "l"]
            
            # Verify units are of the same type before converting
            if (f in dist and t in dist) or (f in mass and t in mass) or (f in vol and t in vol):
                result = val * (factors[f] / factors[t])
                
                # Format the result nicely (e.g., 2 decimal places if you want)
                self.output["text"] = f"Result: {result} {t}"
            else:
                self.output["text"] = "Error: Incompatible units"
                
        except ValueError:
            self.output["text"] = "Error: Please enter a valid number"

if __name__ == "__main__":
    Calculator().mainloop()