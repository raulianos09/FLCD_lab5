class Grammar:
    def __init__(self, faFilename):
        self.__faFilename = faFilename
        self.__initialNonterminal = ""
        self.__nonterminals = []
        self.__terminals = []
        self.__productions = {}

    def getNonterminals(self):
        toPrint = ""
        for x in self.__nonterminals:
            toPrint += x + " "
        return toPrint

    def getInitialNonterminal(self):
        return self.__initialNonterminal

    def setInitialNonterminal(self, newNonTerminal):
        self.__initialNonterminal = newNonTerminal

    def getTerminals(self):
        return self.__terminals

    def getProductions(self):
        return self.__productions

    def getProductionsForNonterminal(self, nonterminal):
        return self.__productions[nonterminal]

    def readFromFile(self):
        faFile = open(self.__faFilename, "r")
        lines = faFile.readlines()
        self.__initialNonterminal = lines[0].strip();
        self.__nonterminals = lines[1].split()
        self.__terminals = lines[2].split()

        for line in lines[3:]:
            if line != "\n":
                nonterminal, production = line.split("=")
                nonterminal = nonterminal.strip()
                production = production.strip()
                if nonterminal not in self.__productions.keys():
                    self.__productions[nonterminal] = [production]
                else:
                    self.__productions[nonterminal].append(production)

        faFile.close()

    def checkCFG(self):
        for key in self.__productions.keys():
            counter = 0
            for nonterminal in self.__nonterminals:
                if nonterminal in key:
                    counter += 1
            if counter > 1:
                return False
        return True
