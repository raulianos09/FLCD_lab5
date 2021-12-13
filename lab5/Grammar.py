class Grammar:
    def __init__(self, faFilename):
        self.__faFilename = faFilename
        self.__initialNonterminal = ""
        self.__nonterminals = []
        self.__terminals = []
        self.__productions = {}
        self.__productionNumbers = {}


    def getAlphabet(self):
        return list(self.getNonterminals()) + list(self.getTerminals())


    def getNonterminals(self):
        return self.__nonterminals


    def getInitialNonterminal(self):
        return self.__initialNonterminal


    def getTerminals(self):
        return self.__terminals


    def getProductions(self):
        return self.__productions


    def getProductionsForNonterminal(self, nonterminal):
        return self.__productions[nonterminal]


    def getProductionsNumbers(self):
        return self.__productionNumbers


    def setInitialNonterminal(self, newNonTerminal):
        self.__initialNonterminal = newNonTerminal
        self.__nonterminals.append(newNonTerminal)


    def setProductions(self, key, value, indexOfValue):
        listOfProductions = []
        currentIndex = 0
        for string in self.__productions[key]:
            if currentIndex == indexOfValue:
                listOfProductions.append(value)
            else:
                listOfProductions.append(string)
            currentIndex += 1

        self.__productions.update({key : listOfProductions})


    def readFromFile(self):
        faFile = open(self.__faFilename, "r")
        lines = faFile.readlines()
        self.__initialNonterminal = lines[0].strip()
        self.__nonterminals = lines[1].split()
        self.__terminals = lines[2].split()

        production_nr = 0
        for line in lines[3:]:
            if line != "\n":
                production_nr += 1
                lhs, rhs = line.split("=")
                lhs = lhs.strip()
                # rhs = list of terminals and/or non-terminals
                rhs = rhs.split()
                self.addProduct(lhs, rhs)
                self.addProductNumber(lhs, rhs, production_nr)

        faFile.close()


    def addProduct(self, lhs, rhs):
        if lhs not in self.__productions.keys():
            self.__productions[lhs] = [rhs]
        else:
            self.__productions[lhs].append(rhs)


    def addProductNumber(self, lhs, rhs, production_nr):
        # here we assign the index number to the production
        self.__productionNumbers[lhs + " = " + str(rhs)] = production_nr


    def checkCFG(self):
        for key in self.__productions.keys():
            counter = 0
            for nonterminal in self.__nonterminals:
                if nonterminal in key:
                    counter += 1
            if counter > 1:
                return False
        return True
