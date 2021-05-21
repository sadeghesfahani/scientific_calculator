class Parse:
    def __init__(self, text):
        self.text = text
        (self.opens, self.closed) = (list(), list())
        self.validate = True
        self.inner_parts = list()
        self.operators = list()
        self.scam()

    def scam(self):
        counter_open = 0
        counter_close = 0
        inner = str()
        open_check = False
        # (self.text[let].isnumberic() and not self.text[let+1].isnumeric())
        for let in range(len(self.text)):
            if self.text[let] == "(":
                open_check = True
                self.opens.append(let)
                counter_open += 1
            elif self.text[let] == ")":
                if open_check:
                    self.closed.append(let)
                    counter_close += 1
                    open_check = False
                    self.inner_parts.append(inner)
                    inner = str()
                else:
                    self.validate = False
            else:
                if let < len(self.text):
                    if self.text[let] in "+-*/":
                        self.operators.append(let)

                if open_check:
                    inner += self.text[let]
        if counter_open == counter_close and self.validate:
            pass
        else:
            print("wrong")


par1 = Parse("35*(4578+8754)+56log(545/23)")
print(par1.inner_parts)
