class State:
    def __init__(self, index):
        # state = list of productions
        self.state = []
        self.index = index

    def addToState(self, production):
        if production not in self.state:
            self.state.append(production)

    def getState(self):
        return self.state

    def getIndex(self):
        return self.index

    def __str__(self):
        printableState = ""
        for prod in self.state:
            printableState += str(prod) + "\n"

        return "State {}: {}".format(self.index, printableState)