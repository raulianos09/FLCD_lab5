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

    def getTerminals(self):
        return self.__terminals

    def getProductions(self):
        return self.__productions

    def getProductionsForNonterminal(self, nonterminal):
        return self.__productions[nonterminal]

    def readFromFile(self):
        faFile = open(self.__faFilename, "r")
        lines = faFile.readlines()
        self.__initialNonterminal = lines[0].split()
        self.__nonterminals = lines[1].split()
        self.__terminals = lines[2].split()

        for line in lines[3:]:
            if line != "\n":
                nonterminal, production = line.split("=")
                if len(production) > 2:
                    production = production[1:-1]
                else:
                    production = production[1:]

                if nonterminal not in self.__productions.keys():
                    self.__productions[nonterminal] = [production]
                else:
                    self.__productions[nonterminal].append(production)


        faFile.close()


    def checkCFG(self):
        for production in self.__productions.keys():
            nrNonterminals = 0
            for nonterminal in self.__nonterminals:
                if nonterminal in self.__productions[production]:
                    nrNonterminals += 1

            if nrNonterminals > 1:
                return False

        return True
