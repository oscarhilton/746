class Phone:
    running =  False
    number = ""
    name =  ""

    def run(self):
        self.running = True
    def setNumber(self, number):
        self.number = number
    def setName(self, name):
        self.name = name
    def reset(self):
        self.running = False
        self.number = ""
        self.name = ""