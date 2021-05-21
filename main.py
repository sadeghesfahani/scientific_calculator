import tkinter as tk


class Calculator:
    def __init__(self):
        number_buttons = dict()
        root = tk.Tk()
        root.title("Calculator")
        main_text = tk.Text(root, height=3, width=54)
        main_text.grid(column=1, row=1,columnspan=4)
        counter = 1
        for button_number in range(10):  # making number buttons
            number_buttons[button_number] = tk.Button(root, text=button_number,
                                                      command=lambda: self.insert(button_number))
            if button_number == 0:
                (column, row) = (1, 8)
            else:
                row = int(7 - button_number // 3.1)
                column = counter

            number_buttons[button_number].grid(column=column, row=row,sticky="ewns")
            counter = counter + 1 if counter % 3 != 0 and button_number != 0 else 1
        dot_button=tk.Button(root, text=".",
                                                      command=lambda: self.insert("."))
        dot_button.grid(column=2, row=8,sticky="ewns")
        plus_button = tk.Button(root, text="+",
                               command=lambda: self.insert("+"))
        plus_button.grid(column=3, row=8, sticky="ewns")
        equal_button = tk.Button(root, text="=",
                                command=lambda: self.insert("="))
        equal_button.grid(column=4, row=8, sticky="ewns")
        multiply_button = tk.Button(root, text="*",
                                 command=lambda: self.insert("*"))
        multiply_button.grid(column=4, row=8, sticky="ewns")
        log_button = tk.Button(root, text="log",
                                    command=lambda: self.insert("log"))
        log_button.grid(column=1, row=2, sticky="ewns")
        main_text.insert(tk.END, "this is gonna be our calculator\nin three \n lines\n")

        root.mainloop()

    def insert(self, data):
        pass


calc1 = Calculator()
