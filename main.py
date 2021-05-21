import tkinter as tk


class Calculator:
    def __init__(self):
        self.input_text = str()
        number_buttons = dict()
        root = tk.Tk()
        root.title("Calculator")
        self.main_text = tk.Entry(root, width=70, textvariable=self.input_text)
        self.main_text.grid(column=1, row=1, columnspan=5)
        counter = 1
        for button_number in range(10):  # making number buttons

            number_buttons[button_number] = tk.Button(root, text=button_number,
                                                      command=lambda txt = button_number: self.insert(txt))
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
                               command=lambda: self.insert("log("))
        log_button.grid(column=5, row=2, sticky="ewns")
        pran1_button = tk.Button(root, text="(",
                               command=lambda: self.insert("("))
        pran1_button.grid(column=1, row=2, sticky="ewns")
        pran2_button = tk.Button(root, text=")",
                                 command=lambda: self.insert(")"))
        pran2_button.grid(column=2, row=2, sticky="ewns")
        delete_button = tk.Button(root, text="<--",
                                  command=lambda: self.insert("<--"))
        delete_button.grid(column=3, row=2, sticky="ewns")
        clean_button = tk.Button(root, text="C",
                                 command=lambda: self.insert("clean"), bg="yellow")
        clean_button.grid(column=4, row=2, sticky="ewns")
        power_button = tk.Button(root, text="^",
                                 command=lambda: self.insert("^"))
        power_button.grid(column=4, row=5, sticky="ewns")
        sqr_button = tk.Button(root, text="sqr",
                               command=lambda: self.insert("sqr("))
        sqr_button.grid(column=5, row=5, sticky="ewns")
        #self.main_text.insert(tk.END, "this is gonna be our calculator\nin three \n lines\n")

        root.mainloop()

    def insert(self, button):
        if button =="clean":
            self.main_text.delete(0, tk.END)
        elif button=="<--":
            current_text = self.main_text.get()[:-1]
            self.main_text.delete(0, tk.END)
            self.main_text.insert(0,current_text)
        else:
            current_text = self.main_text.get()
            self.main_text.delete(0,tk.END)
            self.main_text.insert(0,current_text + str(button))
            # self.main_text.delete("1.0","end")
            # self.main_text.insert(tk.END,current_text+str(button))
            # self.input_text


calc1 = Calculator()
