class State:
    def __init__(self, index):
        self.productions = []
        self.index = index

    def addToState(self, production):
        if production not in self.productions:
            self.productions.append(production)

    def setProductions(self, productions):
        self.productions = productions

    def getState(self):
        return self.productions

    def getProduction(self, index):
        return self.productions[index]

    def getLength(self):
        return len(self.productions)

    def getIndex(self):
        return self.index

    def getProductions(self):
        return self.productions

    def __str__(self):
        printableState = ""
        for prod in self.productions:
            printableState += str(prod) + "\n"

        return "State {}: {}".format(self.index, printableState)

    def __eq__(self, other):
        return self.getProductions() == other.getProductions()

