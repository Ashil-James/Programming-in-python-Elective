from breezypythongui import EasyFrame

class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Calculator")

        self.display = self.addTextField("", row=0, column=0, columnspan=4)

        buttons = ['7','8','9','/',
                   '4','5','6','*',
                   '1','2','3','-',
                   '0','=','+','C']

        row, col = 1, 0
        for b in buttons:
            self.addButton(
                text=b,
                row=row,
                column=col,
                command= self.buttonClicked(b)
            )
            col += 1
            if col > 3:
                col = 0
                row += 1

    def buttonClicked(self, text):
        print("Clicked:", text)

        if text == "C":
            self.display.setText("")
        elif text == "=":
            try:
                self.display.setText(str(eval(self.display.getText())))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.getText() + text)

app = Calculator()
app.mainloop()