from Parser import Parser


class ParsingTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.parser = Parser(self.grammar)
        self.canCol = self.parser.col_can_LR0()
        i = 0
        for state in self.canCol:
            print("State " + str(i) + ": ")
            for prod in state:
                print(prod)
            i = i+1
        self.table = []

    def get_actions(self):
        for state in self.canCol:
            pass

    def action(self,state):
        for production in state:
            cond, nonterminal = self.parser.dot_before_nonterminal(production)
            if cond is True:
                return "shift"
            cond,nonterminal = self.parser.dot_after_nonterminal(production)
            if nonterminal != "S\'":
                return "reduce " + self.canCol.index(state)
            else:
                return "acc"
        return "error"