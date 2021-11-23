from queue import Queue

class Production:
    def __init__(self,lhs,rhs,dot = 0):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = dot #dot position
        # ex: S -> *aSbS =====> lhs = S, rhs = [a,S,b,S], dot = 0

    def __str__(self) -> str:
        return "Production: {} -> {}".format(self.lhs, self.rhs)


class Parser:
    def __init__(self,grammar):
        self.grammar = grammar
        #create augmented grammar
        self.grammar.addProduct("S'", [self.grammar.getInitialNonterminal()])
        self.grammar.setInitialNonterminal("S'")
        self.states = []
        for key in self.grammar.getProductions().keys():
            for production in self.grammar.getProductions()[key]:
                self.grammar.setProductions(key, '.' + production)
        print(grammar.getProductions())


    def closure(self, i):
        c = set(i)
        previousC = set()
        while previousC != c:
            for product in c:
                return



