from breezypythongui import EasyFrame

class MyApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "My First GUI App")
        
        self.addLabel(text = "Enter Name: ", row = 0, column = 0)
        self.inputField = self.addTextField(text ="", row = 0, column = 1,)
        self.outputLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 2)
        self.addButton(text = "Submit", row = 2, column = 0, command = self.process)
        
    def process(self):
        name = self.inputField.getText()
        self.outputLabel["text"] = "Hello "+ name

MyApp().mainloop()