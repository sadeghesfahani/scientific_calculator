class Parse:
    def __init__(self, text):
        self.text = text
        (self.opens, self.closed) = (list(), list())
        self.validate = True
        self.inner_parts = list()
        self.operators = list()
        self.paranteses = list()
        self.blocks=list()
        if self.scam() is not None:
            pass

    def scan(self):
        for block in self.blocks:
            for index in range(block[0],block[1]+1):
                pass


    def scam(self):
        counter_open = 0
        counter_close = 0
        inner = dict()
        open_check = [False, 0]
        # (self.text[let].isnumberic() and not self.text[let+1].isnumeric())
        starter_paranteses = list()

        for let in range(len(self.text)):
            if self.text[let] == "(":
                starter_paranteses.append(let)
            elif self.text[let] == ")":
                try:
                    self.paranteses.append([starter_paranteses[len(starter_paranteses)-1], let])
                    starter_paranteses.pop()
                except:
                    print("format wrong")
        blocks=[set(range(block[0],block[1]+1)) for block in self.paranteses]
        final_blocks=blocks.copy()
        for block in blocks:
            for I in range(len(blocks)):
                if block !=blocks[I]:
                    test=block.intersection(blocks[I])
                    if block.intersection(blocks[I])== block:
                        final_blocks.remove(blocks[I])
        final_blocks1 = [[sorted(list(block))[0], sorted(list(block))[len(block)-1]] for block in final_blocks]
        self.blocks=final_blocks1
        if len(final_blocks1)!=0:
            return True
        else:
            return None

par1 = Parse("35*(4578(25*6)+8754)+56log(545/23)")
print(par1.paranteses)



# [4,9]
