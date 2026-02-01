    # Калькулятор! #

import tkinter as tk

window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x400")

window_input = tk.Entry(
    window,
    width=20,
    justify="right",
    font=("Arial", 16)
)
window_input.grid(row=0, column=0, columnspan=4)

def safe_calculate(expression):
    try:
        allowed_chars = set('0123456789+-*/. ')
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return str(result)
        else:
            return "КАВО?"
    except:
        return "Че у вас тут происходит?"
    
class CalculatorButton:
    
    def press(self):
        if self.button_type == "number":
            window_input.insert(tk.END, self.text)
        elif self.button_type == "operation":
            window_input.insert(tk.END, self.text)  
        elif self.button_type == "clear":
            window_input.delete(0, tk.END)
        elif self.button_type == "equals":
            expression = window_input.get()  # получаем выражение
            result = safe_calculate(expression)  # вычисляем
            window_input.delete(0, tk.END)  # очищаем поле
            window_input.insert(0, result) 

    def __init__(self, window, text, row, column, button_type="number"):

        self.window = window
        self.text = text
        self.row = row
        self.column = column
        self.button_type = button_type
        self.create_button()

    def create_button(self):
        button = tk.Button(self.window, text=self.text, command=self.press)
        button.grid(row=self.row, column=self.column)
    
button0 = CalculatorButton(window, "0", 4, 0, "number")
button1 = CalculatorButton(window, "1", 3, 0, "number")
button2 = CalculatorButton(window, "2", 3, 1, "number")
button3 = CalculatorButton(window, "3", 3, 2, "number")
button4 = CalculatorButton(window, "4", 2, 0, "number")
button5 = CalculatorButton(window, "5", 2, 1, "number")
button6 = CalculatorButton(window, "6", 2, 2, "number")
button7 = CalculatorButton(window, "7", 1, 0, "number")
button8 = CalculatorButton(window, "8", 1, 1, "number")
button9 = CalculatorButton(window, "9", 1, 2, "number")
button_dot = CalculatorButton(window, ".", 5, 0, "number")  # точка

# Операции
button_addition = CalculatorButton(window, "+", 1, 3, "operation")
button_subtraction = CalculatorButton(window, "-", 2, 3, "operation")
button_multiplication = CalculatorButton(window, "*", 3, 3, "operation")
button_division = CalculatorButton(window, "/", 4, 3, "operation")

# Служебные
button_clear = CalculatorButton(window, "C", 4, 1, "clear")
button_equals = CalculatorButton(window, "=", 4, 2, "equals")

window.mainloop()