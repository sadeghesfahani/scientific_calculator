import tkinter as tk


class Calculator:
    def __init__(self):
        self.input_text = str()
        number_buttons = dict()
        root = tk.Tk()
        root.title("Calculator")
        self.main_text = tk.Entry(root, width=54, textvariable=self.input_text)
        self.main_text.grid(column=1, row=1, columnspan=4)
        counter = 1
        for button_number in range(10):  # making number buttons
            number_buttons[button_number] = tk.Button(root, text=button_number,
                                                      command=lambda: self.insert(button_number))
            if button_number == 0:
                (column, row) = (1, 8)
            else:
                row = int(7 - button_number // 3.1)
                column = counter

            number_buttons[button_number].grid(column=column, row=row, sticky="ewns")
            counter = counter + 1 if counter % 3 != 0 and button_number != 0 else 1
        dot_button = tk.Button(root, text=".",
                               command=lambda: self.insert("."))
        dot_button.grid(column=2, row=8, sticky="ewns")
        plus_button = tk.Button(root, text="+",
                                command=lambda: self.insert("+"))
        plus_button.grid(column=3, row=8, sticky="ewns")
        equal_button = tk.Button(root, text="=",
                                 command=lambda: self.insert("="))
        equal_button.grid(column=4, row=8, sticky="ewns")
        multiply_button = tk.Button(root, text="*",
                                    command=lambda: self.insert("*"))
        multiply_button.grid(column=4, row=7, sticky="ewns")
        multiply_button = tk.Button(root, text="/",
                                    command=lambda: self.insert("/"))
        multiply_button.grid(column=4, row=6, sticky="ewns")
        log_button = tk.Button(root, text="log",
                               command=lambda: self.insert("log"))
        log_button.grid(column=1, row=2, sticky="ewns")
        delete_button = tk.Button(root, text="<--",
                                  command=lambda: self.insert("<--"))
        delete_button.grid(column=4, row=5, sticky="ewns")
        clean_button = tk.Button(root, text="C",
                                 command=lambda: self.insert("clean"), bg="yellow")
        clean_button.grid(column=4, row=2, sticky="ewns")
        power_button = tk.Button(root, text="^",
                                 command=lambda: self.insert("^"))
        power_button.grid(column=3, row=2, sticky="ewns")
        sqr_button = tk.Button(root, text="sqr",
                               command=lambda: self.insert("sqr"))
        sqr_button.grid(column=2, row=2, sticky="ewns")
        self.main_text.insert(tk.END, "this is gonna be our calculator\nin three \n lines\n")

        root.mainloop()

    def insert(self, button):
        current_text = self.input_text
        # self.main_text.delete("1.0","end")
        # self.main_text.insert(tk.END,current_text+str(button))
        self.input_text


calc1 = Calculator()
