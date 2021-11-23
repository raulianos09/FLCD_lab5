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
        self.grammar.productions["S'"] = [[self.grammar.getInitialNonterminal()]]
        self.grammar.setInitialNonterminal("S'")
        self.states = []

